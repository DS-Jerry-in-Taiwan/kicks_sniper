import json
import os
import re
import pandas as pd

def extract_har_basic_info(har_path):
    """
    從 HAR 檔案提取所有 request 的 URL、method 及 response 的 status code。
    回傳 list of dict。
    """
    if not os.path.exists(har_path):
        print(f"HAR 檔案不存在: {har_path}")
        return []
    with open(har_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)
    entries = har_data.get("log", {}).get("entries", [])
    result = []
    for entry in entries:
        req = entry.get("request", {})
        res = entry.get("response", {})
        info = {
            "url": req.get("url"),
            "method": req.get("method"),
            "status": res.get("status")
        }
        result.append(info)
    return result

def extract_har_headers(har_path):
    """
    從 HAR 檔案提取所有 request 及 response 的 headers。
    回傳 list of dict，每筆包含 url、request_headers、response_headers。
    """
    if not os.path.exists(har_path):
        print(f"HAR 檔案不存在: {har_path}")
        return []
    with open(har_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)
    entries = har_data.get("log", {}).get("entries", [])
    result = []
    for entry in entries:
        req = entry.get("request", {})
        res = entry.get("response", {})
        info = {
            "url": req.get("url"),
            "request_headers": req.get("headers", []),
            "response_headers": res.get("headers", [])
        }
        result.append(info)
    return result

def extract_har_cookies_payload_body(har_path):
    """
    從 HAR 檔案提取 cookies、payload、response body 等資訊。
    回傳 list of dict，每筆包含 url、request/response cookies、payload、response body。
    """
    if not os.path.exists(har_path):
        print(f"HAR 檔案不存在: {har_path}")
        return []
    with open(har_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)
    entries = har_data.get("log", {}).get("entries", [])
    result = []
    for entry in entries:
        req = entry.get("request", {})
        res = entry.get("response", {})
        info = {
            "url": req.get("url"),
            "request_cookies": req.get("cookies", []),
            "response_cookies": res.get("cookies", []),
            "payload": req.get("postData", {}),
            "response_body": res.get("content", {})
        }
        result.append(info)
    return result

def filter_har_by_url_pattern(har_path, pattern):
    """
    根據關鍵字或 URL pattern 過濾/標記特定 API 回應內容。
    pattern: 可為字串或正則表達式
    回傳 list of dict，僅包含符合 pattern 的 entry。
    """
    if not os.path.exists(har_path):
        print(f"HAR 檔案不存在: {har_path}")
        return []
    with open(har_path, "r", encoding="utf-8") as f:
        har_data = json.load(f)
    entries = har_data.get("log", {}).get("entries", [])
    result = []
    for entry in entries:
        req = entry.get("request", {})
        url = req.get("url", "")
        if re.search(pattern, url):
            result.append(entry)
    return result

def har_entries_to_dataframe(entries, fields=None):
    """
    將 HAR 解析資訊轉為 pandas DataFrame。
    entries: list of dict（如 extract_har_basic_info/extract_har_headers 等回傳）
    fields: 欲保留欄位（list of str），預設全部
    """
    if not entries:
        return pd.DataFrame()
    if fields:
        filtered = [ {k: v for k, v in e.items() if k in fields} for e in entries ]
        return pd.DataFrame(filtered)
    return pd.DataFrame(entries)

if __name__ == "__main__":
    har_file = os.path.join(os.path.dirname(__file__), "../../data/8891_craw_related/auto.8891.com.tw.har")
    # 1. 分析 HAR 結構（列印所有 request/response 資訊）
    print("--- HAR 結構分析 ---")
    basic_info = extract_har_basic_info(har_file)
    print(basic_info[:3])  # 只顯示前3筆
    # 2. 過濾特定 API（例如 URL 包含 'usedauto-newSearch'）
    print("\n--- 過濾特定 API ---")
    filtered_entries = filter_har_by_url_pattern(har_file, r"usedauto-newSearch")
    print(f"符合條件的 entry 數量: {len(filtered_entries)}")
    # 3. 結構化輸出為 DataFrame 並存檔
    print("\n--- DataFrame 輸出 ---")
    df = har_entries_to_dataframe(basic_info)
    print(df.head())
    df.to_csv("data/8891_craw_related/har_basic_info.csv", index=False)
