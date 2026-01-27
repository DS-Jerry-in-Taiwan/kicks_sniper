import sys
import os
import json
import re
import random
import logging
from datetime import datetime
from src.utils.schema import CAR_SCHEMA
import requests
from bs4 import BeautifulSoup

# 設定 logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def analyze_har(har_path):
    """
    讀取 HAR 檔案並分析 request/response 結構，列印主要欄位。
    """
    logging.info(f"開始分析 HAR 檔案: {har_path}")
    if not os.path.exists(har_path):
        logging.error(f"HAR 檔案不存在: {har_path}")
        print(f"HAR 檔案不存在: {har_path}")
        return
    with open(har_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)
    entries = har_data.get("log", {}).get("entries", [])
    logging.info(f"共發現 {len(entries)} 筆 entries")
    for entry in entries:
        req = entry.get("request", {})
        res = entry.get("response", {})
        print("URL:", req.get("url"))
        print("Method:", req.get("method"))
        print("Status:", res.get("status"))
        print("Request Headers:", req.get("headers", []))
        print("Response Headers:", res.get("headers", []))
        print("Request Cookies:", req.get("cookies", []))
        print("Response Cookies:", res.get("cookies", []))
        print("Query String:", req.get("queryString", []))
        print("Post Data:", req.get("postData", {}))
        print("Response Content:", res.get("content", {}))
        print("="*40)

# 可選用代理 IP，格式為 ["http://ip:port", ...]
PROXY_LIST = []
if os.path.exists("proxyIP.csv"):
    try:
        import pandas as pd
        df_proxy = pd.read_csv("proxyIP.csv")
        if "proxyIP" in df_proxy.columns:
            PROXY_LIST = [str(ip) for ip in df_proxy["proxyIP"].dropna().tolist()]
    except ImportError:
        PROXY_LIST = []

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0"
]

def clean_price(price_str):
    # 將 "36.8萬"、"88萬"、"0" 轉為 int 元
    try:
        if not price_str:
            return 0
        price_str = str(price_str).replace(",", "")
        match = re.search(r"([\d\.]+)\s*萬", price_str)
        if match:
            return int(float(match.group(1)) * 10000)
        match = re.search(r"([\d,]+)", price_str)
        if match:
            return int(match.group(1))
        return int(float(price_str))
    except Exception:
        return 0

def clean_mileage(mileage_str):
    # 將 "2.5萬公里"、"25000公里"、"0" 轉為 int 公里
    try:
        if not mileage_str:
            return 0
        mileage_str = str(mileage_str).replace(",", "")
        match = re.search(r"([\d\.]+)\s*萬", mileage_str)
        if match:
            return int(float(match.group(1)) * 10000)
        match = re.search(r"([\d,]+)", mileage_str)
        if match:
            return int(match.group(1))
        return int(float(mileage_str))
    except Exception:
        return 0

def fetch_listings_html(url="https://auto.8891.com.tw/nissan/kicks"):
    car_list = []
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    proxies = None
    if PROXY_LIST:
        proxy = random.choice(PROXY_LIST)
        proxies = {"http": proxy, "https": proxy}
    try:
        logging.info(f"開始抓取列表頁: {url}")
        resp = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        resp.raise_for_status()
        with open("debug_8891.html", "w", encoding="utf-8") as f:
            f.write(resp.text)
        soup = BeautifulSoup(resp.text, "lxml")
        car_items = soup.select(".carList .carInfo")
        logging.info(f"解析到 {len(car_items)} 筆車輛資料")
        # 依據 8891 Nissan Kicks 列表頁結構調整
        for car_item in car_items:
            title = car_item.select_one(".carName")
            year = car_item.select_one(".carYear")
            price = car_item.select_one(".carPrice")
            mileage = car_item.select_one(".carMileage")
            location = car_item.select_one(".carAddress")
            url_tag = car_item.select_one("a")
            car = {
                "id": url_tag["href"].split("-")[-1].replace(".html", "") if url_tag and "href" in url_tag.attrs else "",
                "source": "8891",
                "title": title.text.strip() if title else "",
                "year": int(year.text.strip()[:4]) if year and year.text.strip()[:4].isdigit() else 0,
                "price": clean_price(price.text) if price else 0,
                "mileage": clean_mileage(mileage.text) if mileage else 0,
                "location": location.text.strip() if location else "",
                "url": f"https://auto.8891.com.tw{url_tag['href']}" if url_tag and "href" in url_tag.attrs else "",
                "status": "active",
                "crawl_time": datetime.now().isoformat()
            }
            # 僅保留 title 含 Kicks 的資料
            if "kicks" in car["title"].lower():
                car_list.append(car)
        logging.info(f"最終保留 {len(car_list)} 筆 Kicks 資料")
    except Exception as e:
        logging.error(f"Failed to fetch HTML: {e}")
        print(f"Failed to fetch HTML: {e}")
    return car_list

if __name__ == "__main__":
    logging.info("開始執行 8891 Kicks 列表爬蟲")
    cars = fetch_listings_html()
    logging.info(f"共取得 {len(cars)} 筆車輛資料，準備寫入 kicks_list.json")
    with open("data/raw/kicks_list.json", "w", encoding="utf-8") as f:
        json.dump(cars, f, ensure_ascii=False, indent=2)
    logging.info("寫入完成")
