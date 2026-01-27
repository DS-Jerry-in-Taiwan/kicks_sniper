from notifier import TelegramNotifier

if __name__ == "__main__":
    notifier = TelegramNotifier()
    test_msg = "✅ 測試訊息：Kicks Sniper Telegram Bot 本地測試成功！"
    resp = notifier.send(test_msg)
    print("Status:", resp.status_code)