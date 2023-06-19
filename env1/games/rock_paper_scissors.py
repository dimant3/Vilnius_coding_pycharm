from random import randint

# create a list of play options
play_options = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
# panaudojam importuotą random modulį ir funkcijoje nurodome galimus variantus (0,2)
# turime 3 galimas reikšmes (rock 0, paper 1, scissors 2), Python seka prasideda nuo 0 (ne 1!)
computer = play_options[randint(0,2)]

# set player to False (galimai reikalinga, kad neprasidetu while loop)
player = False

while player == False:
    # set player to true
    player = input("Rock, Paper, Scissors: ") # tik kai ivedama reiksme, player pasikeicia i true
    if player == computer: # cia tikriausiai nurodoma zaidejo eile
        print("Tie!") # jeigu player pasirinkimas sutampa su computer gauname lygiasias
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else: # jeigu irasytas tekstas ne Rock, Paper, Scissors meta klaida
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = play_options[randint(0, 2)]
"""
Once the while loop starts, the computer will patiently wait for you to make a play. As soon as you take your turn,
your status changes from False to True because any value assigned to the variable (kintamasis) player makes player True.
We use the input() function to pass the new value to the variable player. Your input will determine which statement is
triggered below. Using nested if/elif/else statements, we check every possible outcome of the game and return a message
stating the winner, a tie, or an error.
We use else at the end to catch anything that isn't "Rock", "Paper" or "Scissors". Finally we reset the player value
to False to restart the while loop. (Tam gale reikalinga vėl pakartoti player = False, kad ciklas neprasidetu kol
neivesta (input) reiksme.
"""