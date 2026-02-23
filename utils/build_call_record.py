from datetime import datetime


def build_call_record(method: str, ticker: str, time_frame: str, delay_seconds: float) -> dict:
    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "method": method,
        "ticker": ticker,
        "time_frame": time_frame,
        "delay_seconds": delay_seconds,
    }
