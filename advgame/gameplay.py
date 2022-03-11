#!/bin/bash/env python3

"""
Text based adventure game: 
    You bought an old house and strange things start
    happening, what will you do to get out of it?
"""   
def start_game():
    #ask the user what they're name is and ask if they want to play
    name = input('Hello you brave soul! what is your name?')
    ans = input(f'{name}, would you like to play a game? (yes/no)')

    #start the game if they enter yes
    if ans.lower() == 'yes':
        lvl1_options = ["1", "2"]
        lvl1_choice = ""
        while lvl1_choice not in lvl1_options:
            print('''
            You just bought an old 1900s home to renovate with your spouse,
            with the intention of making it your forever home.  The cleaning and demo
            process starts smoothly but you start hearing random banging when no one was home.
            You follow the banging noises to find a hollow wall under the stairs that looks 
            to be concealing something behind it.
            What would you like to do next?
        
            1. Tear down the wall to see what it is
            2. Say not today and leave it as is''')
            lvl1_choice = input("Enter option number: ")

            #deciding to tear down the wall
            if lvl1_choice == '1':
                lvl2_options = ["1", "2"]
                lvl2_choice = ""
                while lvl2_choice not in lvl2_options:
                    print('''
                You decide to tear down the wall and satisfy your curiosity,
                once it's open you see it all looks empty at first glance.  Until you look 
                down and notice a small box shoved in the bottom corner covered in dust.
                What would you like to do next? 
                
                1. Take the box out to inspect
                2. Close the wall back up''')
                    lvl2_choice = input('Enter option number: ')
                    
                    #taking the box out
                    if lvl2_choice == "1":
                        lvl3_options = ["1", "2", "3"]
                        lvl3_choice = ""
                        while lvl3_choice not in lvl3_options:
                            print('''
                You decided to take out the box.  It looks really old and 
                as you brush the dust off you see it is locked and appears to have
                ritual symbols and something in latin engraved around the sides.
                What would you like to do next? 
                
                1. Search the house to find the key
                2. Throw it away
                3. Call for spiritual help''')
                            lvl3_choice = input('Enter option number: ')
                        
                        #option 1: search for the key
                        if lvl3_choice == "1":
                            lvl4_options = ["1", "2"]
                            lvl4_choice = ""
                            while lvl4_choice not in lvl4_options:
                                print('''
                You decided to look around to see if you can find the key, 
                you can't find it on the ground floor. Would you like to keep trying
                to find the key or get rid of the box?
                            
                1. look in the attic for the key
                2. throw the box away''')
                                lvl4_choice = input('Enter option number: ')

                                #option 1: keep looking
                                if lvl4_choice == "1":
                                    print("you decided to keep looking, days later you still don't find it, YOU LOSE!")
                                
                                #option 2: throw the box away
                            else:
                                print("You decided to throw away the box and hope you don't find anything else in the house, you survive!")


                        #option 2: Throw it away
                        elif lvl3_choice == "2":    
                            print("You decided to throw away the box and hope you don't find anything else in the house, you survive!")

                        #option 3: call for spiritual help
                        else:
                            print('''
                 You decided to call for help to eradicate the spirits in
                 your home, now you get to keep your beautiful home without the 
                 spirits, YOU WIN! ''')    

                    #close the wall back up
                    else:
                        print('''
                 You close the wall back up and think you avoided a potentially horrible outcome, GAME OVER!
                 For now.....''')
                            
            #not today and leave it alone
            else:
                print('Smart choice! You probably avoided being haunted, GAME OVER')

#goodbye message if they enter no
    else:
        print("That's too bad, maybe next time")

start_game() 
