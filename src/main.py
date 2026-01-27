from parser import parse_raw_data
from database import DatabaseManager

def main():
    # 1. 讀取 kicks_list.json 並標準化
    cars = parse_raw_data("data/raw/kicks_list.json")
    print(f"解析車輛數量: {len(cars)}")

    # 2. 寫入 SQLite 資料庫
    with DatabaseManager() as db:
        db.save_cars(cars)
    print("資料已寫入 kicks.db")

if __name__ == "__main__":
    main()