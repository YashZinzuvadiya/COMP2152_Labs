import random

# Solution to Week 02 Questions 

choices = ["Rock", "Paper", "Scissors"]

# playerChoice is to save the user input. 
playerChoice = input("Enter your choice (1 - Rock, 2 - Paper, 3 - Scissors): ")

# This changes the data type of playerChoice from string to int
playerChoice = int(playerChoice)

# Error handelling: out of bounds logic
if playerChoice < 1 or playerChoice > 3: 
    print("Error the input should be an integer between 1 and 3!")
else: # if in bound 
    # Determine the winner logic by using if/elif/else
    computerChoice = random.randint (1,3) # for a random number from 1 and 3 

    # Logic for the choices. 
    if playerChoice == computerChoice: 
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3: 
        print("Rock beats Scissors - You Win!!! ")
    elif playerChoice == 2 and computerChoice == 1: 
        print("Paper beats Rock - You Win!!!")
    elif playerChoice == 3 and computerChoice == 2: 
        print("Scissors beats paper - You Win!!!")
    else: 
        print("You lose!!")

