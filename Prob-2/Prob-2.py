# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Jason Markus

'''
Your IPO comment goes here
'''

def main():
    # your code goes here
    # Ask for the person's name
    name = input("What is your name? ")
    # - Ask for the person's hourly wage
    wage = float(input("What is your hourly wage? "))
    # - Ask for the person's hours
    hours = int(input("How many hours per week do you work? "))
    print()
    # - If they worked more than forty hours they get paid time and a half.
    if (hours > 40):
        overtimeWage = wage * 1.5
        overtimeHours = hours - 40
        overtimePay = overtimeWage * overtimeHours

        regularHours = hours - overtimeHours
    else:
        regularHours = hours
    # - The first 40 hours they get their normal wage
    first40 = wage * regularHours
    # - Hours above 40 they get paid 1.5 x their normal wage
    # - The tax rate is 20% on all wages
    if (hours > 40):
        totalPay = first40 + overtimePay
    else:
        totalPay = first40

    taxWithheld = totalPay * 0.2
    # - Medical insurance withheld is 10% on all wages
    medicalWithheld = totalPay * 0.1
    # - Display nicely formatted
    # - The employee's name
    print("Name:\t\t\t", name)
    # - Regular wages
    print("Regular wages:\t\t", first40)
    # - Overtime wages
    if (hours > 40):
        print("Overtime wages:\t\t", overtimeWage)
    # - Total wages
    print("Total wages:\t\t", totalPay)
    # - Tax withholding
    print("Tax Withheld:\t\t", taxWithheld)
    # - Insurance withholding
    print("Insurance Withheld:\t", medicalWithheld)
    # - Take home pay
    print("Take home pay:\t\t", totalPay - (taxWithheld + medicalWithheld))

main()
