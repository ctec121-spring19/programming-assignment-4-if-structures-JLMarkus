# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Jason Markus

def letterGrade(score):
    # your code here
    
    if score == 5:
       grade = "A"
    elif score == 4:
        grade = "B"
    elif score == 3:
        grade = "C"
    elif score == 2:
        grade = "D"
    elif score == 1:
        grade = "F"
    else:
        grade = "F"
    return grade

def unitTest():
    # your test code here
    print(letterGrade(5))
if __name__ == "__main__":
    unitTest()