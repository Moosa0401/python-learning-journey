"""
A Python package is a directory (folder) that groups related Python files together to organize and reuse code. Think of it like a folder on your computer that holds specific tools so your main project stays neat and manageable

https://pypi.org
"""

import cowsay
import sys

def main():
    if len(sys.argv) == 2:
        #.cow => print out cow
        cowsay.cow("hello, " + sys.argv[1])

        #.trex
        cowsay.trex("hello, " + sys.argv[1])
main()