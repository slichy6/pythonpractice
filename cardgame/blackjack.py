#!/usr/bin/env python3

import random

#function to draw 2 random cards and display
def game():
    cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
    value = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    print(random.choice(cards), random.choice(value))

card1= game()
card2 = game()
    
