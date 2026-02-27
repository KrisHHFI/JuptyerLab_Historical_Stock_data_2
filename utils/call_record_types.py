from typing import NotRequired, TypedDict


class CallRecord(TypedDict):
    timestamp: str
    method: str
    ticker: str
    time_frame: str
    delay_seconds: float
    status: NotRequired[str]
    rows: NotRequired[int]
    interval: NotRequired[str]
    csv_path: NotRequired[str]
    error: NotRequired[str]
