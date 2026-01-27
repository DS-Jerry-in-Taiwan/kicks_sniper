# Phase 1 - 開發流程

## 📅 執行步驟

### Step 1: 環境準備 (@INFRA)
1. 初始化 Git Repository。
2. 建立 Python 3.9+ 虛擬環境。
3. 建立目錄結構：`src/crawlers/`, `data/raw/`, `logs/`。
4. 安裝 `requests`, `beautifulsoup4`, `playwright` (備用)。

### Step 2: 架構設計 (@ARCH)
1. 定義 `Car Object` 的 JSON Schema。
2. 設計爬蟲的 Config 結構 (Target URL, Headers)。
3. **Checkpoint 1**: 確認目錄結構與 Schema 定義。

### Step 3: 核心實作 (@CODER)
1. 分析 8891 列表頁 DOM 結構。
2. 撰寫 `crawler_8891.py`：
   - 實作 HTTP Request (模擬 Browser Headers)。
   - 實作 Parsing Logic (提取欄位)。
   - 實作 Cleaning Logic (Regex 處理數值)。
   - 實作 JSON 存檔。

### Step 4: 測試驗證 (@ANALYST)
1. 執行爬蟲腳本。
2. 驗證 `kicks_list.json` 內容正確性。
3. 檢查是否有 IP Ban 或 CAPTCHA 問題。
4. **Checkpoint 2**: 確認數據品質與程式穩定性。

## ⏳ 時間估算
- INFRA: 10 mins
- ARCH: 15 mins
- CODER: 45 mins
- ANALYST: 15 mins
