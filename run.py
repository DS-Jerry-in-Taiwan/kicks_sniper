import argparse
import subprocess
import sys

def run_crawler():
    # 執行爬蟲產生 kicks_list.json
    result = subprocess.run([sys.executable, "src/crawlers/crawler_8891.py"], check=False)
    sys.exit(result.returncode)

def run_push():
    # 執行主流程（解析 kicks_list.json、推播、資料庫更新）
    result = subprocess.run([sys.executable, "src/main.py"], check=False)
    sys.exit(result.returncode)

def main():
    parser = argparse.ArgumentParser(description="Kicks Sniper 統一入口")
    parser.add_argument("--mode", choices=["crawl", "push", "all"], required=True, help="執行模式：crawl=爬蟲, push=推播, all=全流程")
    args = parser.parse_args()

    if args.mode == "crawl":
        run_crawler()
    elif args.mode == "push":
        run_push()
    elif args.mode == "all":
        run_crawler()
        run_push()

if __name__ == "__main__":
    main()