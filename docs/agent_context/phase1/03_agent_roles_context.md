# Phase 1 - Agent 角色職責

## 🏗️ @INFRA (基礎設施)
- **職責**: 負責專案初始化與環境配置。
- **任務**: 
  - 建立 `kicks_sniper` 專案結構。
  - 設定 `.gitignore`。
  - 產出 `requirements.txt`。

## 📐 @ARCH (架構師)
- **職責**: 定義數據規格與模組介面。
- **任務**:
  - 定義 `data_schema.json` (參考 HLD)。
  - 規劃爬蟲模組的函數結構 (e.g., `fetch_page`, `parse_html`, `clean_data`)。

## 💻 @CODER (開發者)
- **職責**: 撰寫實際的 Python 程式碼。
- **任務**:
  - 實作 8891 爬蟲邏輯。
  - 使用 Regex 清洗 `36.8萬` -> `368000`。
  - 處理分頁 (Optional for prototype, focus on page 1 first)。

## 🧪 @ANALYST (測試員)
- **職責**: 驗證產出數據的品質。
- **任務**:
  - 執行爬蟲並檢查 Output。
  - 驗證欄位型別 (Type Check)。
  - 確認沒有抓到廣告車或無效資料。
