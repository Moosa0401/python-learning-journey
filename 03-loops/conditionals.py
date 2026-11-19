"""
if condition :
    do something

>   greater than
>=  greater than or equal
<   less than
<=  less than or equal
==  equivelant
!=  Not equal
"""

def main():
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))

    Compare(x, y)
    OrCompare(x, y)

    score = int(input("Score: "))
    AndCompare(score)


def Compare(x=0, y=0):
    if x < y:
        print("x is less than y")
    elif y > x:
        print("y is greater than")
    else:
        print("x is equal to y")


def OrCompare(x, y):
    if x < y or x > y:
        print("x is not equal to y")
    else:
        print("x is equal to y")


def AndCompare(score):
    if score >= 90 and score <= 100:
        print("Grade: A")
    elif score >= 80 and score < 90:
        print("Grade: B")
    elif score >=70 and score < 80:
        print("Grade: C")
    elif score >= 60 and score < 70:
        print("Grade: D")
    else:
        print("Grade: F")



if __name__ == "__main__":
    main()