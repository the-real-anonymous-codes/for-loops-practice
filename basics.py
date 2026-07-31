# Print "Hello World" n times
n = int(input("enter your number : "))
for i in range(n) :
    print("Hello world!")

# Print natural numbers from 1 to n.
n = int(input("enter your number : "))
for i in range(1,n+1) :
    print(i)

# Reverse for loop — print n down to 1.
n = int(input("enter your number : "))
for i in range(n,0,-1) :
    print(i)

# Print the multiplication table of a number.
n = int(input("enter your number : "))
for i in range(n , (n*10)+1 , n) :
    print(i)

# Sum of first n natural numbers.
n = int(input("enter your number : "))
for i in range(1,n+1) :
    print(sum(int(i)))