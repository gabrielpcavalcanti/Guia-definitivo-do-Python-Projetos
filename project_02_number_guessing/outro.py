from random import randint
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

LOWER_NUMBER: int = 1
HIGHEST_NUMBER: int = 10
MAX_TRIES: int = 5


def create_console() -> Console:
    return Console()


def create_welcome_panel() -> Panel:
    content = Text()
    content.append("Try to guess a number between ", style="white")
    content.append(f"{LOWER_NUMBER}", style="bold cyan")
    content.append(" and ", style="white")
    content.append(f"{HIGHEST_NUMBER}", style="bold cyan")
    content.append(f"\nYou have ", style="white")
    content.append(f"{MAX_TRIES}", style="bold yellow")
    content.append(" tries to guess the right number.", style="white")
    
    return Panel(
        content,
        title="🎲 Guessing Game",
        style="cyan",
        border_style="bright_cyan",
        expand=False
    )


def generate_random_number() -> int:
    return randint(LOWER_NUMBER, HIGHEST_NUMBER)


def get_user_guess(console: Console) -> int | None:
    try:
        guess: int = int(console.input("[cyan]Type a number: [/]"))
        return guess
            
    except ValueError:
        console.print("Please, enter a valid number.", style="red")
        return None
        

def check_guess(guess: int, target: int) -> str:
    if guess == target:
        return 'correct'
    elif guess < target:
        return 'higher'
    else:
        return 'lower'


def display_feedback(console: Console, result: str, tries_left: int) -> None:
    if result == 'higher':
        console.print("📈 It is a higher number", style="blue")
    elif result == 'lower':
        console.print("📉 It is a lower number", style="magenta")
    
    if tries_left > 0:
        console.print(f'Tries left: {tries_left}\n', style="yellow")


def display_game_over(console: Console, won: bool, target: int) -> None:
    if won:
        console.print("\n🎉 You won!", style="bold green")
    else:
        console.print(
            f'\n💔 You lose! The number was [bold]{target}[/]. Try again next time.', 
            style="bold red"
        )


def guessing_game(console: Console) -> None:
    price = generate_random_number()
    tries = MAX_TRIES

    while tries > 0:
        guess = get_user_guess(console)
        
        if guess is None:
            continue
        
        result = check_guess(guess, price)
        
        if result == 'correct':
            display_game_over(console, won=True, target=price)
            break
        
        tries -= 1
        display_feedback(console, result, tries)
        
        if tries == 0:
            display_game_over(console, won=False, target=price)


def main() -> None:
    console = create_console()
    panel = create_welcome_panel()
    
    console.print(panel)
    console.print()

    guessing_game(console)
        
        
if __name__ == "__main__":
    main()