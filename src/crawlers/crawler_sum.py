import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime

SUM_URL = "https://www.sum.com.tw/"

def clean_price(price_str):
    price_str = price_str.replace(",", "")
    match = re.search(r"([\d\.]+)", price_str)
    return int(float(match.group(1)) * 10000) if match else 0

def fetch_sum_kicks():
    resp = requests.get(SUM_URL, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")
    cars = []
    for a in soup.select(".carWrap .carStyle a"):
        the_info = a.select_one(".theInfo")
        if not the_info:
            continue
        model = the_info.select_one(".model")
        if not model or "KICKS" not in model.get_text(strip=True).upper():
            continue
        brand = the_info.select_one(".subj").get_text(strip=True) if the_info.select_one(".subj") else ""
        model_name = model.get_text(strip=True)
        year = 0
        year_tag = the_info.select_one(".year")
        if year_tag:
            try:
                year = int(year_tag.get_text(strip=True))
            except Exception:
                year = 0
        city = the_info.select_one(".city").get_text(strip=True) if the_info.select_one(".city") else ""
        shop = the_info.select_one(".shopN").get_text(strip=True) if the_info.select_one(".shopN") else ""
        price = 0
        price_tag = the_info.select_one(".price .num")
        if price_tag:
            try:
                price = int(float(price_tag.get_text(strip=True)) * 10000)
            except Exception:
                price = 0
        url = ""
        href = a.get("href", "")
        if isinstance(href, str):
            url = href
        elif isinstance(href, list) and href:
            url = str(href[0])
        if url and isinstance(url, str) and not url.startswith("http"):
            url = "https://www.sum.com.tw/" + url.lstrip("/")
        car_id = ""
        if isinstance(url, str):
            match_id = re.search(r"(\d+)", url)
            if match_id:
                car_id = match_id.group(1)
        cars.append({
            "id": car_id,
            "source": "SUM",
            "title": f"{brand} {model_name}",
            "year": year,
            "price": price,
            "mileage": 0,
            "location": f"{city} {shop}".strip(),
            "url": url,
            "status": "active",
            "crawl_time": datetime.now().isoformat()
        })
    return cars

if __name__ == "__main__":
    cars = fetch_sum_kicks()
    with open("data/raw/sum_kicks_list.json", "w", encoding="utf-8") as f:
        json.dump(cars, f, ensure_ascii=False, indent=2)
