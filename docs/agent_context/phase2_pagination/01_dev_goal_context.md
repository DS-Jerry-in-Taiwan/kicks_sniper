# Phase 2.5 - 開發目標：爬蟲分頁擴充 (Side Quest)

**階段**: Phase 2.5 - Pagination
**前置**: Phase 1 Fix (Playwright 爬蟲) & Phase 2 (DB)
**目的**: 突破單頁限制，讓爬蟲能自動翻頁抓取「所有」在架上的 Nissan Kicks 車輛，確保市場監控無死角。

## 🎯 開發目標
1.  **分頁邏輯實作**: 修改 `crawler_8891.py`，加入自動點擊「下一頁」或遍歷頁碼的功能。
2.  **資料聚合**: 確保多頁抓取下來的數據能合併成一個完整的 `kicks_list.json`。
3.  **穩健性增強**: 翻頁時需加入隨機延遲 (Random Sleep)，避免被偵測為異常流量。
4.  **ETL 相容性**: 確保產出的 JSON 格式不變，讓 Phase 2 的 `main.py` 能無痛寫入資料庫。

## 📦 交付物清單
1.  `src/crawlers/crawler_8891.py`: (更新版) 支援多頁爬取的腳本。
2.  `data/raw/kicks_list.json`: (更新版) 包含所有頁面車輛的完整資料。

## ✅ 驗收標準
- [ ] 爬蟲執行後，抓取的車輛總數應顯著增加 (例如 > 30 筆，視當時市場總量而定)。
- [ ] 能夠自動識別「最後一頁」並停止，不會陷入無限迴圈或報錯。
- [ ] 執行過程中無重複資料 (Deduplication handled by script or subsequent ETL)。

