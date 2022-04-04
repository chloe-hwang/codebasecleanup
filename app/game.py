



from random import choice

valid_selections = ["rock", "paper", "scissors"]



#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in valid_selections:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(valid_selections)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#


winner = {
    "rock":{
        "rock": None,
        "paper": "paper",
        "scissors": "rock",
    },
    "paper":{
        "rock": "paper",
        "paper": None, # represents a tie
        "scissors": "scissors",
    },
     "scissors":{
        "rock": "rock",
        "paper": "scissors",
        "scissors": None, # represents a tie
    },
}


    
gamewinner = winner[u][c]

if gamewinner == u:
    print("User Won!")
elif gamewinner == c:
    print("The Computer Won!")
elif gamewinner is None: 
    print("It's a tie!")
