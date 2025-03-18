import time

def time_out():
    for i in range (5, 0, -1):
        print(i)
        time.sleep(1)

score = int(input("Please enter your test score:"))

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
   

score_grade()
print("You score equal is", str(score) + ".")
print("End of program execution")
time_out()
print("END")
