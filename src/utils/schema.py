# Car Object Schema 定義
CAR_SCHEMA = {
    "id": str,
    "source": str,
    "title": str,
    "year": int,
    "price": int,
    "mileage": int,
    "location": str,
    "url": str,
    "status": str,
    "crawl_time": str
}

# 爬蟲主要函數簽名
def fetch_listings(url: str) -> list:
    """抓取列表頁面並回傳車輛資料清單"""
    return []

def parse_item(html_element) -> dict:
    """解析單一車輛 HTML 元素，回傳標準化 dict"""
    return {}

def clean_price(price_str: str) -> int:
    """將價格字串轉為整數"""
    return 0

def clean_mileage(mileage_str: str) -> int:
    """將里程字串轉為整數"""
    return 0
