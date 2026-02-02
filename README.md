# Kicks Sniper

## 專案說明
Kicks Sniper 是一個自動化爬蟲與資料處理框架，支援 8891 Nissan Kicks 車輛資訊抓取、資料推播與資料庫更新。

---

## 目錄結構
```
.
├── src/
│   ├── crawlers/
│   │   └── crawler_8891.py
│   ├── etl.py
│   ├── main.py
│   ├── parser.py
│   ├── database.py
│   └── utils/
├── data/
├── logs/
├── Dockerfile
├── docker-compose.yml
├── kicks_sniper.config   # 版控參數（如 IMAGE_TAG），不含敏感資訊
├── .env                 # 僅本地敏感資訊，不進版控
├── requirements.txt
├── README.md
```

---

## 安裝與建置

### 1. 參數設定
- `kicks_sniper.config`：**唯一進版控的設定檔**，僅放非敏感參數（如 IMAGE_TAG）。
- `.env`：僅本地存放敏感資訊（如 token），**不進版控**。

### 2. 建置 Docker 鏡像
```bash
IMAGE_TAG=$(grep IMAGE_TAG kicks_sniper.config | cut -d'=' -f2) docker compose build kicks-sniper-build
```
- 只需 build kicks-sniper-build，所有 service 共用同一鏡像。

### 3. 啟動服務
- 執行單一流程：
  - 爬蟲：`docker compose up kicks-sniper-crawler`
  - ETL/推播：`docker compose up kicks-sniper-etl`
- 一鍵全流程：
  - `docker compose up kicks-sniper-all`

---

## 主要服務說明（docker-compose.yml）

- **kicks-sniper-build**：僅用於 build 鏡像，不啟動流程。
- **kicks-sniper-crawler**：執行爬蟲，產生 kicks_list.json。
- **kicks-sniper-etl**：執行資料解析、推播、資料庫更新。
- **kicks-sniper-all**：一鍵執行爬蟲與 ETL 全流程。

---

## 參數與安全建議

- **敏感資訊**（如 TELEGRAM_TOKEN）僅放在 `.env`，並加入 `.gitignore`。
- **版控參數**（如 IMAGE_TAG）僅放在 `kicks_sniper.config`，並進版控。
- build 階段用 `IMAGE_TAG=$(grep IMAGE_TAG kicks_sniper.config | cut -d'=' -f2)` 指定，不依賴 .env。

---

## 常見指令

- 建置鏡像（依 kicks_sniper.config 參數）：
  ```bash
  IMAGE_TAG=$(grep IMAGE_TAG kicks_sniper.config | cut -d'=' -f2) docker compose build kicks-sniper-build
  ```
- 啟動單一流程：
  ```bash
  docker compose up kicks-sniper-crawler
  docker compose up kicks-sniper-etl
  ```
- 一鍵全流程：
  ```bash
  docker compose up kicks-sniper-all
  ```

---

## 其他

- 若需調整 build 參數，請直接修改 kicks_sniper.config 並重新 build。
- 若需新增敏感資訊，請僅於本地 .env 設定，勿推送至版控。