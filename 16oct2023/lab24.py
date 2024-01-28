# find the maximum of 3 numbers using ternary operator.

num1 = float(input("enter number one: \n"))
num2 = float(input("enter number two \n"))
num3 = float(input("enter number three \n"))

max_number = num1 if (num1 > num2 and num1 > num3) else (num2 if num2>num3 else num3)
print(f"The maximum {num1}, {num2}, and {num3} is: {max_number}")


