from parser import parse_raw_data
from database import DatabaseManager
from strategy import is_golden_car
from notifier import TelegramNotifier

def main():
    # 1. 讀取 kicks_list.json 並標準化
    cars = parse_raw_data("data/raw/kicks_list.json")
    print(f"解析車輛數量: {len(cars)}")

    # 2. 寫入 SQLite 資料庫，取得新車與降價車
    with DatabaseManager() as db:
        new_cars, updated_cars = db.save_cars(cars)
    print("資料已寫入 kicks.db")
    print(f"新上架: {len(new_cars)}，降價: {len(updated_cars)}")

    # 3. 篩選黃金車並推播
    notifier = TelegramNotifier()
    for car in new_cars:
        if is_golden_car(car):
            # 顯示價格單位為萬（如 42 萬），若價格 < 1000 則直接顯示，否則轉為萬
            price_raw = car.get("price", 0)
            try:
                price = float(price_raw)
                price_str = f"{price:.0f}萬" if price < 1000 else f"{int(price)//10000}萬"
            except Exception:
                price_str = str(price_raw) if price_raw else "電洽"
            msg = f"✨ [新上架] {car['year']} {car['title']}\n價格: {price_str}\n里程: {car['mileage']:,}km\n地點: {car.get('location','')}\n{car.get('url','')}"
            notifier.send(msg)
    for car in updated_cars:
        if is_golden_car(car):
            price_raw = car.get("price", 0)
            try:
                price = float(price_raw)
                price_str = f"{price:.0f}萬" if price < 1000 else f"{int(price)//10000}萬"
            except Exception:
                price_str = str(price_raw) if price_raw else "電洽"
            msg = f"📉 [降價警報] {car['year']} {car['title']}\n新價格: {price_str}\n里程: {car['mileage']:,}km\n地點: {car.get('location','')}\n{car.get('url','')}"
            notifier.send(msg)

if __name__ == "__main__":
    main()
