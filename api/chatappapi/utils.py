from datetime import datetime


def now_as_str() -> str:
    return datetime.now().strftime("%m/%d/%Y %-I:%M %p")
