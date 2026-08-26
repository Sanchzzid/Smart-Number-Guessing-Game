
def calculate_score(attempts_used, max_attempts, multiplier) -> int:
    return (max_attempts - attempts_used + 1) * multiplier

