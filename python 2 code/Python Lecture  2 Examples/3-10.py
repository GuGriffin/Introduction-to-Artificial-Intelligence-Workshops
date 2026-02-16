player1 = int(input("Player 1, please enter: 0 (Scissors), 1 (Rock), 2 (Paper): "))
# Get input from Player 1 and assign it to the variable `player1`

player2 = int(input("Player 2, please enter: 0 (Scissors), 1 (Rock), 2 (Paper): "))
# Get input from Player 2 and assign it to the variable `player2`

if player1 < 0 or player1 > 2 or player2 < 0 or player2 > 2:
    # If either player inputs a number outside the valid range
    print("Please follow the game rules")
    # Output "Please follow the game rules"
else:
    # If inputs are valid
    if ((player1 == 0 and player2 == 2) or
        (player1 == 1 and player2 == 0) or
        (player1 == 2 and player2 == 1)):
        # Conditions where Player 1 wins
        print("Player 1 wins!")
        # Output "Player 1 wins!"
    elif player1 == player2:
        # If Player 1 and Player 2 make the same choice
        print("It's a tie, play again!")
        # Output "It's a tie, play again!"
    else:
        # If Player 2 wins
        print("Player 2 wins!")
        # Output "Player 2 wins!"
