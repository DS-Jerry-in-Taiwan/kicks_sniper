# Kicks Sniper

## 統一入口點

使用 run.py 管理所有流程：

- 執行爬蟲產生 kicks_list.json  
  ```bash
  python run.py --mode crawl
  ```

- 執行推播（解析 kicks_list.json 並推播/更新 kicks.db）  
  ```bash
  python run.py --mode push
  ```

- 一次執行爬蟲+推播全流程  
  ```bash
  python run.py --mode all
  ```

## 目錄結構
- `src/crawlers/crawler_8891.py`：爬蟲腳本，產生 kicks_list.json
- `src/main.py`：主流程（解析、推播、資料庫）
- `run.py`：統一入口，集中管理所有流程