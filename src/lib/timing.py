from datetime import (
    datetime, 
    timedelta, 
    timezone
)
def get_now_time(hours: int = 8) -> datetime:
    return datetime.now(timezone(timedelta(hours=hours)))