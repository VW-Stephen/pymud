from datetime import datetime


def log(message):
    now = datetime.now()
    print(f"[{now}] - {message}")
