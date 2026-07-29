import random

n = int(input("Enter number of times you want to play"))
for i in range(n):
    valid_choice = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(valid_choice)
    user_choice = input("Select your choice (Rock, Paper, Scissors): ").strip().capitalize()


    if user_choice not in valid_choice:
        print("Please enter a valid choice")
        break
    
    
    
    elif computer_choice == user_choice:
        print(f"Computer chose: {computer_choice}")
        result = "Same choice, so Draw"

    elif (computer_choice == "Rock" and user_choice == "Scissors") or \
            (computer_choice == "Paper" and user_choice == "Rock") or \
            (computer_choice == "Scissors" and user_choice == "Paper"):
        print(f"Computer chose: {computer_choice}")
        result = "COMPUTER WON"

    else:
        print(f"Computer chose: {computer_choice}")
        result = "YOU WON"
    
    print(result)
