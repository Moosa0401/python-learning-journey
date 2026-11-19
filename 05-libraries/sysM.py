"""
https://docs.python.org/3/library/sys.html#module-sys
"""

import sys

def main():
    checkArgv()
    # print("hello, my name is", sys.argv[1])
    iterateThrough()

def checkArgv():
    #argv
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
#     elif len(sys.argv) > 2:
#         sys.exit("Too many arguments")

def iterateThrough():
    for arg in sys.argv[1:]:
        print("hello, my name is", arg)


main()