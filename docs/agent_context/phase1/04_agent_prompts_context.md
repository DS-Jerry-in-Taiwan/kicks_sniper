# Phase 1 - Agent Prompts

## @INFRA Prompt
你現在是 Infra Agent。請執行以下任務：
1. 在當前目錄初始化 Python 專案結構：
   - `src/crawlers/`
   - `src/utils/`
   - `data/raw/`
   - `tests/`
2. 建立 `requirements.txt`，包含 `requests`, `beautifulsoup4`, `lxml`, `pandas`, `playwright`。
3. 建立 `.gitignore` 排除 `venv/`, `__pycache__/`, `.env`, `data/`。
完成後請回報目錄結構。

## @ARCH Prompt
你現在是 Arch Agent。請根據 High-Level Design (HLD) 定義數據結構：
1. 在 `src/utils/` 下建立 `schema.py` 或 `const.py`，定義 Car Object 的 Dict 結構。
   - 欄位包含: id, source, title, year, price, mileage, location, url, status, crawl_time。
2. 設計爬蟲的主要 Function Signature，例如 `fetch_listings(url)`, `parse_item(html_element)`。
完成後請觸發 Checkpoint 1。

## @CODER Prompt
你現在是 Coder Agent。請實作 `src/crawlers/crawler_8891.py`：
1. 使用 `requests` + `BeautifulSoup` 嘗試抓取 8891 Nissan Kicks 列表頁。
   - Target URL 請搜尋 8891 Nissan Kicks 的網址。
   - 記得加上 User-Agent Headers 模擬瀏覽器。
2. 實作解析邏輯：
   - 提取 Title, Year, Price, Mileage, Location。
   - **關鍵**: 實作 `clean_price(str)` 和 `clean_mileage(str)` 函數，將 "36.8萬" 轉為 368000 (int)。
3. 將結果存入 `data/raw/kicks_list.json`。
4. 如果 `requests` 被擋（回傳 403/404），請改用 `playwright` 實作。

## @ANALYST Prompt
你現在是 Analyst Agent。請驗證開發成果：
1. 執行 `python src/crawlers/crawler_8891.py`。
2. 檢查 `data/raw/kicks_list.json` 是否存在。
3. 讀取 JSON 檔案，隨機抽樣 3 筆資料，檢查：
   - Price 是否為 Int？
   - Year 是否在合理範圍 (2018-2025)？
   - Title 是否包含 "Kicks"？
4. 輸出簡單的品質報告。
完成後請觸發 Checkpoint 2。
