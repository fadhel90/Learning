# Factorial

# Loop
# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24
# 1! -> 1

number = int(input("Enter the a number\n"))
if number < 0 :
    print("factorial does not work ")
else:
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
        print("fact is ->",fact)

