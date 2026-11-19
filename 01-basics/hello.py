print("Hello, World!")
print("I'm starting my Python learning journey!")

# Ask user for their name
name = input("What is your name? ").title()

# Say hello to user
print("Hello " + name)
print("Hello", name)
print("Hello %s" %(name))
print(f"Hello {name}")

"""
print(*objects, sep=' ', end='\n', file=None, flush=False)¶
"""
# how to avoid new line and space
print("hello ", end="")
print(name)
print("hello", name, sep="???")

# Escaping
print("hello, \"friend\"")
print('hello, "friend"')