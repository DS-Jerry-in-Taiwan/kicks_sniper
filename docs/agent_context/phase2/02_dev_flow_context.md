# Phase 2 - 開發流程

## 📅 執行步驟

### Step 1: 資料庫設計 (@ARCH)
1. 設計 SQLite Schema (`schema.sql`)。
   - `cars` Table: 儲存車輛基本資料 (id, title, year, mileage, url, created_at)。
   - `price_history` Table: 儲存價格變動 (car_id, price, recorded_at)。
2. **Checkpoint 1**: 確認 Table 關聯設計。

### Step 2: 核心實作 (@CODER)
1. 實作 `src/database.py`:
   - `init_db()`: 讀取 schema.sql 建立表格。
   - `upsert_car(car_data)`: 核心邏輯 (檢查是否存在 -> 插入/更新)。
2. 實作 `src/parser.py`:
   - `parse_raw_data(json_file)`: 讀取 Phase 1 的 JSON，回傳標準化的 List[Dict]。
3. 實作 `src/main.py` (ETL Pipeline):
   - 呼叫 Crawler (Phase 1) -> 呼叫 Parser -> 呼叫 Database。

### Step 3: 整合測試 (@ANALYST)
1. 執行 `main.py`。
2. 使用 SQLite Client (或 script) 查詢 `kicks.db`。
3. 驗證資料是否正確入庫。
4. **Checkpoint 2**: 驗證「降價偵測」邏輯是否可行。

## ⏳ 時間估算
- ARCH: 15 mins
- CODER: 60 mins
- ANALYST: 15 mins

