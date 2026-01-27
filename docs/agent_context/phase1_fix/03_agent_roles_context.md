# Phase 1 Fix - Agent 角色職責

## 🏗️ @INFRA (基礎設施)
- **專注任務**: Playwright 環境建置.
- **指令**: `pip install playwright && playwright install chromium`.

## 📐 @ARCH (架構師)
- **專注任務**: 指導 Coder 從 Sync (Requests) 轉向 Async (Playwright).
- **決策**: 必須使用 `headless=True` (開發與 CI 標準).

## 💻 @CODER (開發者)
- **專注任務**: 重寫 `src/crawlers/crawler_8891.py`.
- **重點**: 確保能抓到動態載入後的 DOM 元素。

## 🧪 @ANALYST (測試員)
- **專注任務**: 透過「截圖」與「數據筆數」來驗證修復結果。
