# Phase 2 - Checkpoint 協議

## 🚦 Checkpoint 1: Schema 設計確認 (After @ARCH)
**檢查重點**:
1. Table 設計是否符合需求？(`cars` + `price_history`)
2. `car_id` 的定義方式？(是使用 8891 的原始 ID 還是我們自己生 UUID？建議直接用 `source + raw_id` 組合鍵以防衝突)。

**決策**:
- ✅ **通過**: 進入開發。
- 🔄 **修改**: 若沒考慮到多平台 ID 衝突，請 Arch 修正 Primary Key 設計。

---

## 🚦 Checkpoint 2: 價格追蹤邏輯驗證 (After @ANALYST)
**情境測試**:
1. 第一次執行：抓到車 A (35萬)。
2. **手動修改** 爬蟲回傳值：把車 A 改成 33萬。
3. 第二次執行。

**檢查重點**:
- `cars` 表中，車 A 的價格是否變為 33萬？
- `price_history` 表中，車 A 是否有兩筆紀錄 (35萬, 33萬)？

**決策**:
- ✅ **通過**: 系統具備降價監控能力，Phase 2 完成。
- ❌ **失敗**: 若只有一筆紀錄或沒更新，請 @CODER 修正 `upsert` 邏輯。

