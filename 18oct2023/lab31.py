#task 1

#Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
#input- score - 89
#output- B
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59
#If, elif, else

score = int(input("enter your grade: "))

if score >=90 and score<=100:
    print ("Grade A")
elif score >=80 and score<89:
    print("Grade B")
elif score >=70 and score <79:
    print("Grade C")
elif score >=60 and score <69:
    print("Grade D")
elif score >=0 and score <59:
    print("Grade F")
else:
    print("postive intger required")

