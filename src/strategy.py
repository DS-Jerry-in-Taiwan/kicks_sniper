def is_golden_car(car: dict) -> bool:
    """
    黃金參數篩選：
    - 年份 2020 或 2021
    - 里程 50000~80000
    - 價格 < 42 萬（單位：萬）
    """
    try:
        year = int(car.get("year", 0))
        mileage = int(car.get("mileage", 0))
        # 支援價格單位為萬（如 42 表示 42 萬）
        price = float(car.get("price", 0))
        # 若價格小於 1000，視為單位萬，轉換為元
        if price < 1000:
            price = int(price * 10000)
        else:
            price = int(price)
        return (year in [2020, 2021]) and (50000 <= mileage <= 80000) and (price < 420000)
    except Exception:
        return False
