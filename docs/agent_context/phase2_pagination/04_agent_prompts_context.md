# Phase 2.5 - Agent Prompts

## @ARCH Prompt
你現在是 Arch Agent。請分析 Playwright 的分頁策略：
1. 8891 的下一頁按鈕通常是 `a.next` 或 `button.next`。
2. 請指導 Coder 使用 "While Loop" 結構。
3. **重要策略**: 換頁後，必須等待 DOM 更新。建議的 Pattern 是：
   - `old_first_item = await page.inner_text('.car-item-title')`
   - `click_next_page()`
   - `wait_for_function(lambda: current_first_item != old_first_item)`
   - 或者簡單一點：`await page.wait_for_timeout(3000)` (雖然笨但有效)。

## @CODER Prompt
你現在是 Coder Agent。請修改 `src/crawlers/crawler_8891.py` 支援分頁：
1. 初始化 `all_cars = []`。
2. 進入 `while True` 迴圈：
   - 呼叫解析函式，將當前頁面車輛加入 `all_cars`。
   - 印出 "已抓取第 X 頁，目前累積 Y 筆"。
   - 嘗試尋找「下一頁」按鈕：
     - 如果按鈕存在且 `display != none`：
       - `await button.click()`
       - `await page.wait_for_timeout(random.randint(2000, 4000))` (隨機等待 2-4秒)
     - 如果按鈕不存在或 disabled：
       - `print("已達最後一頁")`
       - `break`
3. 迴圈結束後，將 `all_cars` 寫入 `data/raw/kicks_list.json`。

## @ANALYST Prompt
你現在是 Analyst Agent。請驗證分頁成果：
1. 執行爬蟲，觀察 Console Log 是否有 "Page 2", "Page 3" 的紀錄。
2. 檢查產出的 `kicks_list.json`：
   - `len(data)` 是否大於 30？(單頁通常 20-30 筆)。
   - 抽查最後一筆資料，是否真的屬於最後一頁的車？
3. 執行 `python src/main.py` 確保資料庫能正確吃進這些大量資料。

