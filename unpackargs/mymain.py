#!/usr/bin/env python3
#Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

from jrpg import find # work assigned to the junior programmer (functions)

EXCLUDE = ["/usr", "/home", "/var"] ## Don't search in these locations

def getuserinput():
    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    lookwhere = input("What is the path in which I should search? ")
    return (lookfor, lookwhere)

def main():
    """runtime code"""
    while(True):
        print("Results: ",find(*getuserinput(),EXCLUDE)) # call function with argument unpacking
        if (input("\nPress n to quit or any other key to search again").lower() == "n"):
            break

main()

