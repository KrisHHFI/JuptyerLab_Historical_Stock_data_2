from utils.call_record_types import CallRecord


def print_calls_made(calls_made: list[CallRecord]) -> None:
    for call in enumerate(calls_made, start=1):
        print(f"{call}")
