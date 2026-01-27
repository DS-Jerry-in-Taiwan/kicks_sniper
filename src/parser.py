import json
from typing import List, Dict, Any

def parse_raw_data(json_file: str) -> List[Dict[str, Any]]:
    """
    讀取 kicks_list.json，轉換為標準化 Dict 清單
    - car_id 格式: source_id (如 8891_4270800)
    - 欄位型別轉換與預設值處理
    """
    with open(json_file, "r", encoding="utf-8") as f:
        raw = json.load(f)
    cars = []
    for item in raw:
        car_id = f"{item.get('source', '8891')}_{item['id']}"
        cars.append({
            "id": car_id,
            "source": item.get("source", "8891"),
            "title": item.get("title", ""),
            "year": int(item.get("year", 0)),
            "price": int(item.get("price", 0)),
            "mileage": int(item.get("mileage", 0)),
            "location": item.get("location", ""),
            "url": item.get("url", ""),
            "status": item.get("status", "active"),
        })
    return cars