def get_input(word_type:str, type=str) -> str| None:
    
    while True:
        
        text = type(input(f"Enter a {word_type}: "))
        
        # rejeita vazio
        if not text:
            print("It can be an empty Value.")
            continue

        # rejeita boolean
        if text.lower() in ("true", "false"):
            print("Do not type a boolean (true/false).")
            continue

        # rejeita número
        try:
            float(text)
            print("Do not type a number.")
            continue
        except ValueError:
            pass  # não é número, o

        return text

def main() -> None:
       
    noun_01 = get_input("noun")
    adjective_01 = get_input("adjective") 
    verb_01 = get_input("verb")
    noun_02 = get_input("noun")
    verb_02 = get_input("verb")

    story = f"""
    Once upon a time, there was a {adjective_01} {noun_01} who loved to {verb_01} all day.

    One day, {noun_02} walked into the room and caught the {noun_01} in the act. 

    {noun_02}: "What are you doing?"
    {noun_01}: "I'm just {verb_01}ing, what's the big deal?"
    {noun_02}: "Well, it's not every day that you see a {noun_01} {verb_01}ing in the middle of the day."
    {noun_01}: "I guess you're right. Maybe I should take a break."
    {noun_02}: "That's probably a good idea. Why don't we go {verb_02} instead?"
    {noun_01}: "Sure, that sounds like fun!"

    And so, {noun_02} and the {noun_01} went off to {verb_02} and had a great time. 

    The end.

    """

    print(story)
    

if __name__ == "__main__":
    main()
    