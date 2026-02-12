from random import randint

def get_dice_numbers(rolls_dice: int) -> list[int]:
    return [randint(1,6) for _ in range(rolls_dice)]


def get_user_input() -> str | None:

    try:
        times: str = input("How many dice would you like to roll? ")
        return times
    
    except (ValueError, EOFError, KeyboardInterrupt):
        print("\nExiting the game. Thanks for playing!")

        return None
    

def validate_and_convert(user_input: str) -> int | None:
    
    try:
        rolls_dice = int(user_input)
        
        if rolls_dice <= 0:
            print("Please, enter a number greater than 0.")
            return None
        
        return rolls_dice
    
    except ValueError:
        print("Please, enter a valid number.")
        return None

def main() -> None:

    while True:

        times = get_user_input()

        if times is None:
            break

        if times.lower().strip() == "exit":
            print("Thanks for playing!")
            break
        
        rolls_dice = validate_and_convert(times)
            
        if rolls_dice is None:
            continue

        dice_numbers = get_dice_numbers(rolls_dice)
        
        print(*dice_numbers, sep=", ")


if __name__ == '__main__':
    main()
