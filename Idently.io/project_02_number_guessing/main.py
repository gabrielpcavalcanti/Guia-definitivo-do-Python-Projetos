from random import randint
from rich.console import Console
from rich.panel import Panel

LOWER_NUMBER:int = 1
HIGHEST_NUMBER:int = 10
MAX_TRIES: int = 5

console = Console()

def generate_random_number() -> int:
    return randint(LOWER_NUMBER, HIGHEST_NUMBER)


def get_user_guess() -> int | None:

    try:
        guess: int = int(input("Type a number: "))
        return guess
            
    except ValueError:
        print("Please, enter a valid number.")
        return None
        

def check_guess(guess: int, target: int) -> str:

    if guess == target:
        return 'correct'
    
    elif guess < target:
        return 'higher'
    
    else:
        return 'lower'


def display_feedback(result: str, tries_left: int) -> None:
    
    if result == 'higher':
        print("It is a higher number")

    elif result == 'lower':
        print("It is a lower number")
    
    if tries_left > 0:
        console.print(f'\nTries left: {tries_left}\n', style="yellow")


def display_game_over(won: bool, target: int) -> None:
    
    if won:
        console.print("\nYou won!", style="green")
    else:
        console.print(f'\nYou lose! The number was [black]{target}[/]. Try again next time.', style="#f22800")


def guessing_game() -> None:

    price = generate_random_number()
    tries = MAX_TRIES

    while tries > 0:

        guess = get_user_guess()
        
        
        if guess is None:
            continue
        
        result = check_guess(guess, price)
        
        if result == 'correct':
            display_game_over(won=True, target=price)
            break
        
        tries -= 1
        display_feedback(result, tries)
        
        if tries == 0:
            display_game_over(won=False, target=price)


def main() -> None: 

    panel = Panel(f"""Try to guess a number between {LOWER_NUMBER} and {HIGHEST_NUMBER}\nYou have {MAX_TRIES} tries to guess the right number.\n""",
                  title="Guessing Game", style="white", expand=False, height=4)
    
    console.print(panel)

    guessing_game()
        
        
if __name__ == "__main__":
    main()
