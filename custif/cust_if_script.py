#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

message = "You recieved a grade of: "
# wrap connection in a float() to accept decimals as numbers
grade = float(input("What did you score on your last test?"))

# if input value was higher or equal to 25
if grade > 100:
    print("not a valid grade")
elif grade >= 90:
    print( message + "A")
elif grade >= 80:
    print(message + "B")
elif grade >= 70:
    print(message + "C")
elif grade >= 60:
    print(message + "D")
elif grade <= 59:
    print(message + "F")    
else:
    print("exiting...")

