#ask the user what they're name is
name = input("Hello brave adventurer! what is your name?")
#give the option to play or quit
ans = input(f"{name}, would you like to go on a quest? (yes/no)")

#start the game if they enter yes
if ans.lower() == "yes":
    print("You have woken up disoriented in an unknown room")
    lvl1 = input("what would you like to do next? \n1. explore the room \n2.cry out for help \n Enter 1 or 2:")
    if lvl1 == "1":
        print("You get up and start looking around the room, you discover a note on the desk by you and a window that is cracked open slightly")
        lvl2 = input("What do you want to do next: \n 1. read the note \n2. try and escape out of the window \n Enter 1 or 2:")
    else:
        print("your cries for help have alerted the bad guys, YOU LOSE!")

else:
    print("That's too bad, maybe next time")
