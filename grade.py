score = input("What is the test score?") 
score = int(score)

if score >= 90:
    print("Your grade is an A")

elif score >= 80:
    print("Your grade is an B")
elif score >= 70:
    print("Your grade is a C")
elif score >= 60:
    print("Your grade is a D")
elif score >= 50:
    print("Your grade is a F")
else:
    print("Next time study more")