import sqlite3
from contextlib import contextmanager
from typing import List, Dict, Any

DB_PATH = "data/kicks.db"
SCHEMA_PATH = "src/schema.sql"

class DatabaseManager:
    def __init__(self, db_path=DB_PATH, schema_path=SCHEMA_PATH):
        self.db_path = db_path
        self.schema_path = schema_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def _init_db(self):
        with open(self.schema_path, "r", encoding="utf-8") as f:
            schema_sql = f.read()
        self.conn.executescript(schema_sql)

    def save_cars(self, cars: List[Dict[str, Any]]):
        for car in cars:
            self.upsert_car(car)

    def upsert_car(self, car: Dict[str, Any]):
        cur = self.conn.cursor()
        car_id = car["id"]
        price = car["price"]

        # 檢查是否已存在
        cur.execute("SELECT price FROM cars WHERE id = ?", (car_id,))
        row = cur.fetchone()

        if row is None:
            # 新車，插入 cars 與 price_history
            cur.execute(
                """INSERT INTO cars (id, source, title, year, price, mileage, location, url, status)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    car["id"], car["source"], car["title"], car["year"], car["price"],
                    car["mileage"], car.get("location", ""), car.get("url", ""), car.get("status", "active")
                ),
            )
            cur.execute(
                "INSERT INTO price_history (car_id, price) VALUES (?, ?)",
                (car_id, price)
            )
        else:
            old_price = row["price"]
            if old_price != price:
                # 價格變動，更新 cars 並新增 price_history
                cur.execute(
                    "UPDATE cars SET price=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                    (price, car_id)
                )
                cur.execute(
                    "INSERT INTO price_history (car_id, price) VALUES (?, ?)",
                    (car_id, price)
                )
            else:
                # 價格未變，只更新 updated_at
                cur.execute(
                    "UPDATE cars SET updated_at=CURRENT_TIMESTAMP WHERE id=?",
                    (car_id,)
                )