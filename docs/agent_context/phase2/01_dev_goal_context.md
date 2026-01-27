# Phase 2 - 開發目標：資料清洗與儲存

**階段**: Phase 2 - Data Pipeline
**前置**: Phase 1 (已產出 raw data)
**目的**: 建立 ETL 流程的 "Transform" 與 "Load" 環節，將原始數據標準化並存入資料庫，以支援歷史價格追蹤。

## 🎯 開發目標
1. **資料庫設計**: 使用 SQLite 建立 `cars` 與 `price_history` 資料表。
2. **資料清洗 (Parser)**: 實作標準化邏輯 (去除文字、轉換型別、生成指紋 ID)。
3. **資料儲存 (Storage)**: 實作 "Upsert" (更新或插入) 邏輯：
   - 若車輛 ID 不存在 -> Insert。
   - 若車輛 ID 存在且價格變動 -> Update 並記錄歷史。
4. **去重機制**: 確保同一台車不會重複存入。

## 📦 交付物清單
1. `src/database.py`: 資料庫連線與操作類別 (Database Manager)。
2. `src/parser.py`: 資料清洗與轉換模組。
3. `data/kicks.db`: 實際生成的 SQLite 資料庫檔案。
4. `src/main.py`: (初步整合) 串接 Crawler -> Parser -> Storage 的主程式。

## ✅ 驗收標準
- [ ] `kicks.db` 成功建立，且包含 schema 定義的 Tables。
- [ ] 能成功讀取 Phase 1 的 `kicks_list.json` 並寫入 DB。
- [ ] 若重複執行寫入，資料庫不會產生重複資料 (Idempotency)。
- [ ] 模擬價格變動 (手動改 JSON 價格) 後再執行，DB 能記錄下新價格。

