# Phase 1 - 驗證清單

## 環境驗證
- [ ] Python 版本 >= 3.9
- [ ] 必要套件 (requests, bs4) 安裝成功
- [ ] 目錄結構符合規範

## 功能驗證
- [ ] 爬蟲腳本能正常執行結束 (Exit code 0)
- [ ] 成功產出 `data/raw/kicks_list.json`
- [ ] JSON 檔案大小 > 0KB

## 數據品質驗證
- [ ] **Schema Check**: 所有欄位 (id, title, price...) 都存在
- [ ] **Type Check**: Price 和 Mileage 必須是 Integer
- [ ] **Value Check**: 
  - Price > 100,000 (排除異常低價)
  - Year > 2017 (Kicks 上市年份)
- [ ] **Logic Check**: 沒有重複的 ID (若有需去重)

## 效能/反爬驗證
- [ ] 單次執行時間 < 30秒
- [ ] 沒有觸發 CAPTCHA 或 IP Ban
