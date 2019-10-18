from datetime import datetime


def log(message: str):
    now = datetime.now()
    print(f"[{now}] - {message}")
