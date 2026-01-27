# Phase 1 - Checkpoint 協議

## 🚦 Checkpoint 1: 架構確認 (After @ARCH)
**觸發時機**: 完成數據 Schema 定義與目錄規劃後。
**檢查重點**:
1. `src/` 目錄結構是否合理？
2. `data_schema` 是否包含 HLD 規定的所有欄位 (特別是 crawl_time, status)？
3. 是否預留了數據清洗 (Cleaning) 的邏輯位置？

**決策選項**:
- ✅ **通過**: 進入 @CODER 開發。
- 🔄 **修正**: Schema 欄位不足，請 @ARCH 補齊。

---

## 🚦 Checkpoint 2: 數據品質確認 (After @ANALYST)
**觸發時機**: 第一次成功產出 JSON 檔案後。
**檢查重點**:
1. **數據是否真的抓到了？** (不能是空的 [] )。
2. **清洗是否成功？** (Price 欄位不能是字串 "36.8萬"，必須是數字 368000)。
3. **反爬狀況**: 是否需要切換到 Playwright？

**決策選項**:
- ✅ **通過**: Phase 1 結束，準備 Phase 2。
- ❌ **失敗 (被擋)**: 請 @CODER 改寫為 Playwright 版本。
- 🔄 **修正 (清洗失敗)**: Regex 寫錯，請 @CODER 修正 Regex。
