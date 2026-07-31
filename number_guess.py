import random
secret_num = random.choice(range(101))
print(secret_num)

for i in range (5) :
    guess_num = int(input("Enter your guess number: "))
    if guess_num == (secret_num):
        print("YOU WON YOU DOMINATED THE WHOLE GAME")
        break
    
    elif  guess_num > secret_num  :
        print("You went higher, come to a lower value")
    
    else:
        print("You went to a lower value, come to a higher value")
