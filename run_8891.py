import logging
import json
from src.crawlers.crawler_8891 import fetch_listings_html

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

if __name__ == "__main__":
    logging.info("Starting to fetch listings HTML from 8891...")
    cars = fetch_listings_html()
    logging.info(f"Fetched {len(cars)} car listings. Writing to kicks_list.json...")
    
    with open("data/raw/kicks_list.json", "w", encoding="utf-8") as f:
        json.dump(cars, f, ensure_ascii=False, indent=4)
    logging.info("Finished writing to kicks_list.json")