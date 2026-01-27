# Phase 1 Fix - Agent Prompts

## @INFRA Prompt
你現在是 Infra Agent (Fix Mode)。
目標：升級環境以支援瀏覽器自動化。
1. 更新 `requirements.txt` 加入 `playwright`。
2. 執行安裝指令。
3. 執行 `playwright install chromium`。
4. 建立 `logs/` 資料夾。

## @ARCH Prompt
你現在是 Arch Agent (Fix Mode)。
目標：設計 Playwright 爬蟲架構。
1. 指示 Coder 使用 `asyncio`。
2. 規範 User-Agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"。
3. 規範等待策略：使用 `page.wait_for_selector` 而非 `time.sleep`。

## @CODER Prompt
你現在是 Coder Agent (Fix Mode)。
目標：使用 Playwright 重寫 `src/crawlers/crawler_8891.py`。
1. 引入 `asyncio`, `playwright.async_api`.
2. 實作 `main()`:
	- 啟動 chromium browser.
	- `context = await browser.new_context(...)` 設定 UA.
	- `page = await context.new_page()`.
	- `await page.goto(url)`.
	- `await page.wait_for_selector('.car-item')` (請確認 8891 實際 class).
	- `await page.screenshot(path='logs/debug_8891.png')`.
	- 解析資料並存檔 JSON。

## @ANALYST Prompt
你現在是 Analyst Agent (Fix Mode)。
目標：驗證修復是否有效。
1. 執行新腳本。
2. 檢查 `logs/debug_8891.png`: 畫面是否正常？(非白畫面/Access Denied).
3. 檢查 `data/raw/kicks_list.json`: 資料筆數是否 > 0？
