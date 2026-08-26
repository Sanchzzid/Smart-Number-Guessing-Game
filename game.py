from random import randint
from utils import *

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
    for attempts_used in range(1, game_option["attempts"]):
        user_guess = input(f"Enter your guess {YELLOW}({attempts_used}/{game_option['attempts']}){RESET}> ")
        user_guess = input_validator(user_guess)
        if user_guess == -1:
            continue
        if user_guess == CORRECT_ANSWER:
            print(f"{GREEN}(+) Yay! you got it in {attempts_used} attempts!!{RESET}")
            score = calculate_score(attempts_used, game_option["max"], game_option["multiplier"])
            print(f"Your score: {score} points")
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
        print(f"{BLUE}:) Thanks for playing!{RESET}")
        break

