def enforce_call_limit(calls_made_count: int, call_limit: int) -> None:
    if calls_made_count >= call_limit:
        raise RuntimeError(
            f"Call limit reached ({calls_made_count}/{call_limit}). Execution terminated."
        )
