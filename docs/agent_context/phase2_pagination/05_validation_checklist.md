# Phase 2.5 - 驗證清單

## 功能驗證
- [ ] 爬蟲能成功識別並點擊「下一頁」
- [ ] 爬蟲能在「最後一頁」自動停止，不會 Crash
- [ ] 執行過程中包含隨機延遲 (Random Sleep)

## 數據驗證
- [ ] `kicks_list.json` 包含多頁合併後的資料
- [ ] 資料總筆數符合預期 (例如網頁顯示 85 筆，JSON 應接近 85 筆)
- [ ] 沒有明顯的重複資料 (Duplicate IDs in JSON)

## 整合驗證
- [ ] 執行 `main.py` 後，SQLite 資料庫中的 `cars` 表格數量增加

