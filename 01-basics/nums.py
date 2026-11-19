"""
types = int, float
+   => add
-   => subtract
*   => multiply
/   => division
//  => floor division
%   => modulo 
"""

# Input function always returns str so you need to cast when you deal with nums
x = float(input("Enter the first value: "))
y = float(input("Enter the second value: "))


# Methods

#round(number, ndigits=None)¶
z = round(x + y)
m = x / y

# Print the result
# print(x + y)
print(f"{z:,}")
print(f"{z:.2f}")
