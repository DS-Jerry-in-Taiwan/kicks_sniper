import asyncio
import json
import re
import logging
import sys
import random
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from src.utils.schema import CAR_SCHEMA
except ImportError:
    CAR_SCHEMA = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

from src.utils.price_config import SPECIAL_PRICE_STRINGS

def clean_price(price_str):
    try:
        if not price_str:
            logging.info(f"Price parse: 空字串，回傳空")
            return ""
        # 去除所有空白、換行、全形空白
        price_str = str(price_str).replace(",", "").replace("", "").replace("\n", "").replace("\r", "").replace(" ", "").strip()
        # 若為特殊字串直接回傳
        if price_str in SPECIAL_PRICE_STRINGS:
            logging.info(f"Price parse: 特殊字串「{price_str}」，直接回傳")
            return price_str
        match = re.search(r"([\d\.]+)萬", price_str, re.DOTALL)
        if match:
            val = float(match.group(1))
            logging.info(f"Price parse: 正常解析「{price_str}」=> {val} (單位:萬)")
            return val
        match = re.search(r"([\d\.]+)", price_str)
        if match:
            val = float(match.group(1))
            logging.info(f"Price parse: 正常解析「{price_str}」=> {val} (單位:萬)")
            return val
        val = float(price_str)
        logging.info(f"Price parse: 正常解析「{price_str}」=> {val} (單位:萬)")
        return val
    except Exception as e:
        logging.warning(f"Price parsing error: {price_str} -> {e}")
        return price_str

def clean_mileage(mileage_str):
    try:
        if not mileage_str:
            return 0
        mileage_str = str(mileage_str).replace(",", "").strip()
        match = re.search(r"([\d\.]+)\s*萬", mileage_str)
        if match:
            return int(float(match.group(1)) * 10000)
        match = re.search(r"([\d,]+)", mileage_str)
        if match:
            return int(match.group(1).replace(",", ""))
        return int(float(mileage_str))
    except Exception as e:
        logging.warning(f"Mileage parsing error: {mileage_str} -> {e}")
        return 0

async def handle_popup(locator):
    logging.info("🛡️ 偵測到定位彈窗，嘗試關閉...")
    try:
        # 優先點擊關閉鈕或拒絕鈕
        close_btn = locator.page.locator(".positionAuthModal_position-auth-modal-close__PsSRY, .tracking-virtual-reject-auth-modal-button")
        if await close_btn.is_visible():
            await close_btn.click()
            logging.info("🛡️ 已點擊 close/reject 關閉彈窗")
            return
        # 再嘗試點擊 mask
        mask = locator.page.locator(".positionAuthModal_position-auth-modal-mask__34NyF")
        if await mask.is_visible():
            await mask.click()
            logging.info("🛡️ 已點擊 mask 關閉彈窗")
            return
        # 最後模擬 ESC
        await locator.page.keyboard.press("Escape")
        logging.info("🛡️ 已按 ESC 關閉彈窗")
    except Exception as e:
        logging.warning(f"⚠️ 關閉彈窗失敗: {e}")

async def fetch_listings_playwright(url="https://auto.8891.com.tw/nissan/kicks"):
    car_list = []
    page_num = 1

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1920, "height": 1080},
            permissions=[]
        )
        page = await context.new_page()
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            await page.wait_for_selector(".car-item, .carList, [class*='car'], [class*='Card']", timeout=15000)
            await page.add_locator_handler(page.locator(".positionAuthModal"), handle_popup)
            await page.wait_for_timeout(3000)
            while True:
                logging.info(f"=== 處理第 {page_num} 頁 ===")
                car_items = await page.query_selector_all('div#items-box a.listItem_row-item__kj_nW.row-item')
                logging.info(f"找到 {len(car_items)} 個車輛項目")
                if not car_items:
                    break
                for idx, item in enumerate(car_items):
                    try:
                        title_elem = await item.query_selector('.listItem_ib-info-title__1xDet .listItem_ib-it-text__l8bxc')
                        title = await title_elem.inner_text() if title_elem else ""
                        if not title:
                            title_elem = await item.query_selector('.listItem_ib-info-title__1xDet')
                            title = await title_elem.inner_text() if title_elem else ""
                        price_elem = await item.query_selector('.listItem_ib-price__W_88B b')
                        if not price_elem:
                            price_elem = await item.query_selector('.listItem_ib-price__W_88B')
                        price_text = await price_elem.inner_text() if price_elem else ""
                        price = clean_price(price_text)
                        icons = await item.query_selector_all('.listItem_ib-icon__uVwM4')
                        year = 0
                        mileage = 0
                        for icon in icons:
                            icon_text = await icon.inner_text()
                            if "年" in icon_text:
                                year_match = re.search(r'(\d{4})', icon_text)
                                if year_match:
                                    year = int(year_match.group(1))
                            elif "公里" in icon_text or "萬" in icon_text:
                                mileage = clean_mileage(icon_text)
                        location_elem = await item.query_selector('.listItem_ib-ii-item__ngmuX')
                        location = await location_elem.inner_text() if location_elem else ""
                        car_url = await item.get_attribute("href")
                        if car_url and not car_url.startswith("http"):
                            car_url = f"https://auto.8891.com.tw{car_url}"
                        car_id = ""
                        if car_url:
                            id_match = re.search(r'infos-(\d+)\.html', car_url)
                            if id_match:
                                car_id = id_match.group(1)
                        car = {
                            "id": car_id or f"8891_{page_num}_{idx}",
                            "source": "8891",
                            "title": title.strip(),
                            "year": year,
                            "price": price,
                            "mileage": mileage,
                            "location": location.strip(),
                            "url": car_url,
                            "status": "active",
                            "crawl_time": datetime.now().isoformat()
                        }
                        if "kicks" in car["title"].lower():
                            car_list.append(car)
                    except Exception as e:
                        logging.error(f"解析車輛項目 {idx} 時發生錯誤: {e}")
                        continue
                # 分頁判斷與點擊
                next_li = await page.query_selector('li.ant-pagination-next')
                if not next_li:
                    logging.info("未找到下一頁按鈕，結束分頁。")
                    break
                is_disabled = await next_li.get_attribute('aria-disabled')
                if is_disabled == "true":
                    logging.info("已到最後一頁，結束分頁。")
                    break
                next_btn = await page.query_selector('li.ant-pagination-next button.ant-pagination-item-link')
                if not next_btn:
                    logging.info("未找到下一頁按鈕，結束分頁。")
                    break

                # 分頁前優先嘗試關閉彈窗
                try:
                    await page.evaluate("""
                        () => {
                            const closeBtn = document.querySelector('.positionAuthModal_position-auth-modal-close__PsSRY') || document.querySelector('.tracking-virtual-reject-auth-modal-button');
                            if (closeBtn) closeBtn.click();
                            const mask = document.querySelector('.positionAuthModal_position-auth-modal-mask__34NyF');
                            if (mask) mask.click();
                        }
                    """)
                    await page.keyboard.press("Escape")
                except Exception as e:
                    logging.info(f"分頁前自動關閉彈窗失敗: {e}")

                await next_btn.click()
                page_num += 1
                await page.wait_for_timeout(random.randint(2000, 5000))
                await page.wait_for_selector('div#items-box a.listItem_row-item__kj_nW.row-item', timeout=10000)
        except Exception as e:
            logging.error(f"抓取過程發生錯誤: {e}")
            try:
                await page.screenshot(path="logs/debug_8891_error.png", full_page=True)
            except:
                pass
        finally:
            await browser.close()
    return car_list

async def main():
    logging.info("開始執行 8891 Kicks 列表爬蟲（Playwright 版本，支援分頁）")
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("logs").mkdir(parents=True, exist_ok=True)
    cars = await fetch_listings_playwright()
    output_path = "data/raw/kicks_list.json"
    logging.info(f"共取得 {len(cars)} 筆車輛資料，準備寫入 {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(cars, f, ensure_ascii=False, indent=2)
    logging.info(f"寫入完成，檔案位置: {output_path}")
    if cars:
        logging.info("資料摘要:")
        logging.info(f"- 總筆數: {len(cars)}")
        valid_price_count = sum(1 for c in cars if isinstance(c["price"], (int, float)) and c["price"] > 0)
        logging.info(f"- 有效價格數: {valid_price_count}")
        logging.info(f"- 有效里程數: {sum(1 for c in cars if c['mileage'] > 0)}")
    else:
        logging.warning("⚠️ 未抓取到任何資料，請檢查截圖 logs/debug_8891.png 進行除錯")

if __name__ == "__main__":
    asyncio.run(main())