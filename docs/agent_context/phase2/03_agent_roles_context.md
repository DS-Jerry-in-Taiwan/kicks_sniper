# Phase 2 - Agent 角色職責

## 🏗️ @INFRA
- **任務**: 
  - 安裝 SQLite 瀏覽工具 (可選，如需 CLI 驗證)。
  - 確保 `data/` 目錄權限可寫入 DB 檔案。

## 📐 @ARCH
- **任務**: 
  - 定義 Database Schema (ER Model)。
  - 設計「價格變動偵測」的演算法邏輯 (是覆蓋舊資料還是新增一筆 History？)。
  - **決策**: 建議採用 `cars` (最新狀態) + `price_history` (歷史紀錄) 雙表設計。

## 💻 @CODER
- **任務**: 
  - 撰寫 Python 的 `sqlite3` 操作程式碼。
  - 實作 Context Manager (`with Database() as db:`) 以確保連線關閉。
  - 將 Phase 1 的爬蟲整合進 `main.py`。

## 🧪 @ANALYST
- **任務**: 
  - 撰寫 SQL 查詢腳本，驗證資料完整性。
  - 測試邊界情況：
    - 空 JSON 寫入會怎樣？
    - 價格為 NULL 會怎樣？
    - 同一台車如果下架了怎麼標記？(Phase 2 先做 Status='sold' 欄位預留)。

