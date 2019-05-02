# Module 3
#   Programming Assignment 4
#     Prob-5.py

# Jason Markus

def main():
    try:
        x = eval(2)
    except TypeError:
        print("x:", x)
    else:
        print("Invalid coefficient given")
except:
    print("/nOops! Something went wrong.")

main()