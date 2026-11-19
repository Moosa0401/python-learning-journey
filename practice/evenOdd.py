"""
to check wether even or odd we use Modulo %

even: if x % 2 == 0 
odd:  if x % 2 != 0
"""

def main():
    x = int(input("What's x? "))
    print(IsEven(x))

    score = int(input("Score: "))

def IsEven(num):
    # if num % 2 == 0: return True
    # else:   return False

    # return True if num % 2 == 0 else False

    return num % 2 == 0

# Match == switch in c++

def MatchCompare(score):
    match score:
        case 90:
            print("A")
        case 80:
            print("B")
        case _:         # default
            print("what?")
        
        


main()
