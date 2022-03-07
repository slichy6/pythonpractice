#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   sys - basic argument parsing"""

# standard libarary import
import sys

args = sys.argv                     # define an args object from values passed in during runtime
print("Username: " + args[1])       # the value in the 1st position is the 1st argument
print("Password: " + args[2])
print("IP Address: " + args[3])
print("Gateway: " + args[4])
print("Oh by the way, your script is named:", args[0]) # position 0 is the name of the script called

