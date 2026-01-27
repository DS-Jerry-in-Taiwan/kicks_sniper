# Phase 2 - 驗證清單

## 結構驗證
- [ ] `src/database.py` 存在且可執行
- [ ] `src/schema.sql` 定義正確
- [ ] `data/kicks.db` 檔案已建立 (SQLite 格式)

## 功能驗證 (ETL)
- [ ] **E (Extract)**: 能成功呼叫 Phase 1 爬蟲取得資料
- [ ] **T (Transform)**: Parser 能處理型別 (str -> int)
- [ ] **L (Load)**: 資料能寫入 DB，無 SQL Error

## 邏輯驗證 (核心)
- [ ] **ID 唯一性**: 同一台車在 `cars` 表中只有一筆資料
- [ ] **歷史紀錄**: 當 JSON 價格改變並再次執行時，`price_history` 應增加一筆紀錄
- [ ] **最新價格**: `cars` 表中的價格應永遠是最新抓到的價格

