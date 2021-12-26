# Python program to to print the factorial of a number.

# storing a number for Factorial in the variable 'num'
num = int(input("Enter a number for factorial - "))
fact = 1
# adding if-elif-else statements
if num < 0:
    print("Invalid")
elif num == 0:
    print("1")
else:
    for i in range(1, num + 1):
        fact = fact * i
print(f"Factorial of {num} is: ", fact)
