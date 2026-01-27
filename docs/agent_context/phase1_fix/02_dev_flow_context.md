# Phase 1 Fix - 開發流程

## 📅 執行步驟

### Step 1: 環境升級 (@INFRA)
1. 讀取 `requirements.txt`，加入 `playwright`，移除 `requests` (視需求保留).
2. 執行 `pip install` 更新環境.
3. **關鍵**: 執行 `playwright install chromium` 安裝瀏覽器核心。

### Step 2: 架構重構 (@ARCH)
1. 分析 Playwright Async API 結構.
2. 定義新的 `main()` 流程：Browser -> Context -> Page -> Goto -> Wait -> Extract.
3. **Checkpoint 1**: 確認 Playwright 架構設計。

### Step 3: 程式碼重寫 (@CODER)
1. 備份舊版 `crawler_8891.py` (可改名為 `crawler_8891_legacy.py`).
2. 撰寫新版 `crawler_8891.py`：
	- 實作 `asyncio` 非同步邏輯.
	- 加入 `User-Agent` 偽裝.
	- 加入 `page.wait_for_selector` 等待清單載入.
	- 加入 `page.screenshot`.

### Step 4: 驗證修復 (@ANALYST)
1. 執行新版爬蟲.
2. 檢查 `logs/` 截圖與 `data/` JSON.
3. **Checkpoint 2**: 確認修復是否成功。

## ⏳ 時間估算
- INFRA: 5 mins
- ARCH: 5 mins
- CODER: 30 mins
- ANALYST: 10 mins
