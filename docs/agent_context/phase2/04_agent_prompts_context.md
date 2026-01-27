# Phase 2 - Agent Prompts

## @ARCH Prompt
你現在是 Arch Agent。請設計 Kicks Sniper 的資料庫 Schema (SQLite)：
1. 需要兩個表：
   - `cars`: 存放車輛靜態屬性 (id [PK], source, title, year, mileage, location, url, status, created_at, updated_at)。
   - `price_history`: 存放價格時間軸 (id [PK], car_id [FK], price, recorded_at)。
2. 請產出 `src/schema.sql`。
3. 思考：如何判斷這筆資料是「新車」還是「舊車降價」？請在 Checkpoint 1 說明邏輯。

## @CODER Prompt
你現在是 Coder Agent。請實作 ETL 流程：
1. 建立 `src/database.py`：
   - 類別 `DatabaseManager`。
   - 方法 `save_cars(cars_list)`：這是最核心的方法。
     - 遍歷列表，對每一台車：
     - 如果 DB 沒這 ID -> Insert `cars` & Insert `price_history`.
     - 如果 DB 有這 ID 且 價格不同 -> Update `cars.updated_at` & Insert `price_history`.
     - 如果 DB 有這 ID 且 價格相同 -> Update `cars.updated_at` (代表還活著).
2. 建立 `src/parser.py`：
   - 負責把 `kicks_list.json` 髒資料轉成乾淨的 Dict。
3. 建立 `src/main.py`：串接 Crawler -> Parser -> Database。

## @ANALYST Prompt
你現在是 Analyst Agent。請進行資料驗證：
1. 執行 `python src/main.py`。
2. 檢查 `data/kicks.db` 是否產生。
3. 寫一個腳本 `scripts/check_db.py`，印出：
   - 目前總車輛數。
   - 價格變動過的車輛數 (count(price_history) > 1)。
4. 確認沒有重複 ID 的車輛 (Duplicate Key)。

