
# Ask for user's name
def main():
    name = input("What's your name: "). title(). strip()
    # Call hello function we created
    Hello(name)

    x = int(input("Enter a numver to be squared: "))
    print(Square(x))


# Definition
def Hello(name = "World"):
    print(f"Hello {name}👋")

# Return keyword:

def Square(x):
    return x**2




# Call main if this file is running
if __name__ == "__main__":
    main()