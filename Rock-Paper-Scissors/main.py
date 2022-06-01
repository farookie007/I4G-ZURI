import random


GAME_OPTIONS = {'R': "ROCK", 'S': "SCISSORS", 'P': "Paper"}     # this defines the choices available in the game by mapping the initials of each options to its value
GAME_RESULTS = {    # this defines what happens by combining the player and computer choice to determine who win and message to print
    'RS': "blunts",
    'PR': "covers",
    'SP': "cuts",
}

h = "#################################################################"     # just for design
print(f"""{h}
{'Welcome to ROCK-PAPER-SCISSORS'.center(len(h))}
{h}""")

while True:     # starting the game loop
    player = input("\n\tR - ROCK\n\tP - PAPER\n\tS - SCISSORS\nMake your play: ").upper()   # the player makes his/her play
    computer = random.choice(list(GAME_OPTIONS.keys()))     # the computer makes its play by randomly choosing one of the game options


    if not GAME_OPTIONS.get(player):
        print("[-] Invalid Option. Please Try Again!")
        continue

    print(f"Player ({GAME_OPTIONS.get(player)}) : CPU ({GAME_OPTIONS.get(computer)})")      # printing the players choices
    # starting the game logic
    if player == computer:  # asks the player to try again if it is a tie
        print("\nIt is a TIE. Play Again.")
        continue
    else:
        determinant = player + computer     # this is the determinant that the player won by forming the winning keys of the player in `GAME_RESULTS`

        if GAME_RESULTS.get(determinant):   # if the determinant exists in the key i.e the player won
            print("\n\tYou WON!!!")
        else:   # if the deterrminant does not exist i.e the computer won
            determinant = determinant[::-1]     # reverses the determinant to make a match
            print("\n\tYou LOSE!!!")

        print(f"\n\t{GAME_OPTIONS.get(determinant[0])} {GAME_RESULTS.get(determinant)} {GAME_OPTIONS.get(determinant[1])}")     # prints the right message based on the determinant.
        break
