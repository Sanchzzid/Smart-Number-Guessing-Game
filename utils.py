
RESET  = "\x1b[0m"
YELLOW = "\x1b[33m"
RED    = "\x1b[31m"
ORANGE = "\x1b[34m"
GREEN  = "\x1b[32m"
BLUE   = "\x1b[35m"

game_settings = {
    1: {"max": 50, "attempts": 10, "multiplier": 1},
    2: {"max": 100, "attempts": 7, "multiplier": 2},
    3: {"max": 200, "attempts": 5, "multiplier": 3}
}


def calculate_score(attempts_used, max_attempts, multiplier) -> int:
    return (max_attempts - attempts_used + 1) * multiplier

def input_validator(user_guess) -> int:
    try:
        user_guess = int(user_guess)
        return user_guess
    except ValueError:
        print(f"{RED}(x) Not a valid number!{RESET}")
        return -1

