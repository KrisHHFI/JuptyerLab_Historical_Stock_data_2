def print_calls_made(calls_made: list[dict]) -> None:
    print("\nCalls made:")
    for index, call in enumerate(calls_made, start=1):
        print(f"{index}. {call}")
