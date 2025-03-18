import time

def time_out():
    for i in range (5, 0, -1):
        print(i)
        time.sleep(1)

def score_grade():
    if score >= 80:
        print ("Your grade is A.")
    elif score >=75:
        print ("Your grade is A-.")
    elif score >=70:
        print ("Your grade is B.")
    elif score >=65:
        print ("Your grade is B-.")
    elif score >=60:
        print ("Your grade is C.")
    elif score >=55:
        print ("Your grade is C-.")
    elif score >=50:
        print ("Your grade is D.")
    else:
        print ("Your grade is F.")
   
score = int(input("Please enter your test score:"))

if 0 <= score <= 100:
    score_grade()
    print("Your score is", str(score) + "." )
else:
    print("You entered an incorrect score.")

print("End of program execution")
time_out()
print("END")
