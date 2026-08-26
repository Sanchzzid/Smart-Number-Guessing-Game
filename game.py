from random import randint

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


running = True

print(f"{BLUE}Welcome to the Number Guessing Game!{RESET}")

while running:
    difficulty_input = input(f"Select difficulty: {GREEN}[1] Easy{RESET}  {YELLOW}[2] Medium{RESET}  {RED}[3] Hard{RESET} > ").lower()
    game_option = None

    if difficulty_input in ["1", "easy"]:
        game_option = game_settings[1]
    elif difficulty_input in ["2", "medium"]:
        game_option = game_settings[2]
    else:
        game_option = game_settings[3]

    CORRECT_ANSWER = randint(1, game_option["max"])

    print(f"\nI'm thinking of a number between 1 and {game_option['max']}.")
    for i in range(game_option["attempts"]):
        user_guess = input(f"Enter your guess {YELLOW}({i+1}/{game_option['attempts']}){RESET}> ")

        try:
            user_guess = int(user_guess)
        except ValueError:
            print(f"{RED}(x) Not a valid number!{RESET}")
            continue

        if user_guess == CORRECT_ANSWER:
            print(f"{GREEN}(+) Yay! you got it!!{RESET}")
            break
        else:
            if user_guess > CORRECT_ANSWER:
                print(f"{ORANGE} ^ Too high! Try lower.{RESET}")
            else:
                print(f"{ORANGE} v Too low! Try higher.{RESET}")
    else:
        print(f"{RED}Attempts exhausted!{RESET}")

    play_again = input(f"\n{YELLOW}Play again? (y/n):{RESET} ").lower().strip()
    if play_again != "y":
        print(f"{BLUE} :) Thanks for playing!{RESET}")
        break


