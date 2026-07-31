import random

n = int(input("Enter number of times you want to play : "))
for i in range(n):
    valid_choice = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(valid_choice)
    user_choice = input(f"Select your choice {valid_choice}: ").strip().capitalize()


    if user_choice not in valid_choice:
        print("Please enter a valid choice")
        break
    
    elif computer_choice == user_choice:

        result = "Same choice, so Draw"

    elif (computer_choice == "Rock" and user_choice == "Scissors") or \
            (computer_choice == "Paper" and user_choice == "Rock") or \
            (computer_choice == "Scissors" and user_choice == "Paper"):
        
                result = "COMPUTER WON"

    else:

        result = "YOU WON"
    print(f"Computer chose: {computer_choice}")
    print(result)
