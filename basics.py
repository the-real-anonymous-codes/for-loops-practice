# print("Q1] Print","Hello World", "n times.")
# n = int(input("enter your number : "))
# for i in range(n) :
#     print("Hello world")
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q2] Print natural numbers from 1 to n.")
# n = int(input("enter your number : "))
# for i in range(1,n+1) :
#     print(i)
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q3] Reverse for loop — print n down to 1.")
# n = int(input("enter your number : "))
# for i in range(n,0,-1) :
#     print(i)
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q4] Print the multiplication table of a number.")
# n = int(input("enter your number : "))
# for i in range(1,11) :
#     print(f"{n} x {i} = {n*i}")
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q5] Sum of first n natural numbers.")
# s = 0
# n = int(input("enter your number : "))
# for i in range(n+1) :
#     s = s+ i
# print(s)
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q6] Factorial of a number.")
# f = 1
# n = int(input("Enter your number : "))
# for i in range(1,n+1):
#     f = f * i
# print(f)
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q7] Print sum of all even and odd numbers in a range separately.")
# n = int(input("Enter your number : "))
# odd_sum = 0
# even_sum = 0 
# for i in range (n+1):
#     if i % 2 == 0 :
#         even_sum = even_sum + i
#     else :
#         odd_sum = odd_sum + i 
# print(f"The sum of even numbers in range is {even_sum} and the sum of odd numbers in range is {odd_sum}")
# # --------------------------------------------------------------------------------------------------
# print()    
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q8] Print all factors of a number.")
# n = int(input("Enter your number : "))
# for i in range (1 ,n+1):
#     if n % i == 0 :
#         print(i)
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q9] Check if a number is perfect (sum of factors = the number itself).")
# n = int(input("enter your number : "))
# s = 0 
# for i in range (1 ,n):
#     if n % i == 0 :
#         s = s + i 
# if s == n :
#     print("Your number is perfect ")
# else :
#     print("Your number is not perfect")
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q10] Check if a number is prime.")
# f = 0
# n = int(input("Enter your number : "))
# for i in range (1 ,n+1):
#     if n % i == 0 :
#         f =  f + 1
# if n == 1 or n == 0:
#     print(f"{n} is  nether prime nor composite")
# elif f == 2 :
#     print(f"{n} is prime number")
# else :
#     print(f"{n} is composite number ")
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q11]  Check if a string is a palindrome.")
# s = input("enter your string : ")
# rev = ""
# for i in range (len(s)-1,-1,-1):
#     rev = rev + (s[i])
# if rev == s :
#     print("Your string is palindrome")
# else :
#     print("Your string is not palindrome")

# print()
# print()
print("Q12] Count letters, digits, and special symbols in a string.")

print("METHOD1")
s = input("enter your string : ")

char = 0
spchar = 0
digits = 0

for i in s:
    if i.isdigit():
        digits = digits + 1
    
    elif i.isalpha():
        char = char + 1
    
    else :
        spchar = spchar + 1

print(f"Number of digits in string: {digits} Number of letters in string: {char} Number of special symbols in string: {spchar}")
# --------------------------------------------------------------------------------------------------  
print()
print()
# --------------------------------------------------------------------------------------------------
print("METHOD 2")
s = input("enter your string : ")

char = 0
spchar = 0
digits = 0
for i in s :
    if ord(i) in range(48,58):
        digits = digits + 1
    elif ord(i) in range(97,123) or ord(i) in range(65,91) :
        char = char + 1
    else :
        spchar = spchar + 1
print(f"Number of digits in string: {digits} Number of letters in string: {char} Number of special symbols in string: {spchar}")
# # --------------------------------------------------------------------------------------------------
# print()
# print()
# # --------------------------------------------------------------------------------------------------
# print("Q13] Reverse a string without using built-in functions.")
# s = input("enter your string : ")
# rev = ""
# for i in range (len(s)-1,-1,-1):
#     rev = rev + (s[i])
# print(rev)

