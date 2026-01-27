# Phase 2.5 - 開發流程

## 📅 執行步驟

### Step 1: 分析分頁機制 (@ARCH)
1.  觀察 8891 列表頁的分頁行為：
    -   是用 URL 參數 (`&page=2`)？
    -   還是必須點擊「下一頁」按鈕 (Button Click)？
    -   **Playwright 策略**: 建議優先嘗試「點擊下一頁按鈕」並等待 API/DOM 更新，這通常比拼湊 URL 更穩健。

### Step 2: 實作迴圈邏輯 (@CODER)
1.  修改 `crawler_8891.py` 的 `main` 函式：
    -   將「抓取單頁」封裝為 `parse_current_page()`。
    -   建立 `while True` 迴圈：
        -   執行 `parse_current_page()` 並 extend 到 `all_cars` 列表。
        -   檢查「下一頁」按鈕是否存在且可點擊 (Enabled)。
        -   若有：點擊 -> 等待載入 (wait_for_selector) -> `time.sleep(random)` -> 繼續。
        -   若無：`break` 跳出迴圈。
    -   最後一次性寫入 `kicks_list.json`。

### Step 3: 整合驗證 (@ANALYST)
1.  執行爬蟲。
2.  檢查 JSON 總筆數。
3.  執行 `src/main.py` (Phase 2 的 ETL)，確認資料能正確寫入 SQLite。

## ⏳ 時間估算
-   ARCH: 10 mins
-   CODER: 40 mins
-   ANALYST: 10 mins

