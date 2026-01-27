-- cars table: 儲存車輛靜態屬性（最新狀態）
CREATE TABLE IF NOT EXISTS cars (
    id TEXT PRIMARY KEY,              -- 組合鍵: source + 原始ID
    source TEXT NOT NULL,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    price INTEGER NOT NULL,
    mileage INTEGER NOT NULL,
    location TEXT,
    url TEXT,
    status TEXT DEFAULT 'active',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- price_history table: 儲存價格歷史紀錄
CREATE TABLE IF NOT EXISTS price_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id TEXT NOT NULL,             -- 對應 cars.id
    price INTEGER NOT NULL,
    recorded_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(car_id) REFERENCES cars(id)
);

-- 索引加速查詢
CREATE INDEX IF NOT EXISTS idx_price_history_car_id ON price_history(car_id);