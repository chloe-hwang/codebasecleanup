



from random import choice


def determine_winner(user_choice, computer_choice):
    #return "paper"
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice
    #return "OOPS"



if __name__ == "__main__":



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



    winner = determine_winner(u,c)
    if winner == u:
        print("User won")
    elif winner == c:
        print("The Computer Won!")
    elif winner is None: 
        print("It's a tie!")

        
