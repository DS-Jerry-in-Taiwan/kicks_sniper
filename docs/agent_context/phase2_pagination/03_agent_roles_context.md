# Phase 2.5 - Agent 角色職責

## 🏗️ @INFRA
-   **任務**: 無特殊需求，維持現有環境。

## 📐 @ARCH
-   **任務**: 
    -   確認 8891 的分頁 Selector (例如 `.page-box .next` 或類似結構)。
    -   定義「換頁成功」的判斷標準 (例如：點擊後，第一台車的 ID 發生變化，或 loading spinner 消失)。

## 💻 @CODER
-   **任務**: 
    -   **核心**: 改寫 `crawler_8891.py`。
    -   **關鍵細節**: 
        -   使用 `page.locator('text=下一頁')` 或對應 class 尋找按鈕。
        -   務必在點擊後加入 `await page.wait_for_timeout(2000)` 或更聰明的等待，防止抓到舊資料。
        -   列印 Log: "Processing Page 1...", "Processing Page 2..." 以便除錯。

## 🧪 @ANALYST
-   **任務**: 
    -   驗證抓回來的資料是否有「跨頁重複」的問題。
    -   確認總數量是否符合 8891 網頁上顯示的「共有 xx 筆」。

