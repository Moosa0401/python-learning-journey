"""
https://docs.python.org/3/library/string.html#module-string
"""
name = input("What's your name?")

'''
String methods
'''
# Remove whitespace from str, lower all the letters and captilize uers's name
name = name.strip().lower().title()


#split user name into first name and last name
first_name, last_name = name.split(" ")


# Say hello to user
print(f"hello, {name}")