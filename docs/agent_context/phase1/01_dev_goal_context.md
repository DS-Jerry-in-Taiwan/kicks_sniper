# Phase 1 - 開發目標：8891 爬蟲原型

**階段**: Week 1 - 爬蟲原型開發
**目的**: 驗證數據擷取可行性，並產出清洗後的標準化數據

## 🎯 開發目標
1. **環境建置**: 建立 Python 虛擬環境與安裝必要套件 (Requests, BeautifulSoup, Playwright)。
2. **數據擷取**: 針對 8891 中古車網進行爬取，目標鎖定 "Nissan Kicks"。
3. **數據清洗**: 將價格、里程、年份等欄位正規化為整數。
4. **輸出產物**: 產出符合 Schema 定義的 `data/raw/kicks_list.json`。

## 📦 交付物清單
1. `src/crawlers/crawler_8891.py`: 核心爬蟲腳本。
2. `data/raw/kicks_list.json`: 抓取下來的測試數據 (至少 10 筆)。
3. `requirements.txt`: 專案依賴。

## ✅ 驗收標準
- [ ] 爬蟲能成功繞過或處理 8891 的基本反爬（若有）。
- [ ] 輸出的 JSON 格式必須包含：id, title, year, price, mileage, location, url。
- [ ] Price 與 Mileage 必須是 Integer 格式（去除 "萬"、"元"、","）。
- [ ] 程式執行過程中無崩潰報錯。
