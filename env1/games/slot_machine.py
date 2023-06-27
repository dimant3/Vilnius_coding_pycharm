import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# describing how many rows and columns our slot machine got
ROWS = 3
COLS = 3

# specify how much symbols are in our cols (reels)
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# to be clear if user bets on 1 row it's top row, 2 - top two, 3 - all the lines
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # we're looping through every row, essentially, that we're going to be checking that the user bet on
    for line in range(lines):
        # symbol we want to check is whatever symbol is in the first column of the current row because all the
        # symbols need to be the same.
        symbol = columns[0][line]
        # now we need to loop through every single column and check for that symbol.
        for column in columns:
            # we go to each column, and we say the symbol to check is equal to the column at the current row that
            # we are looking at.
            symbol_to_check = column[line]
            # we then check if these symbols are not the same. If they are not the same, we break out. which means
            # we are going to check next line.
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):  # cia tikrai nesuprantu iki galo, kaip simboliai yra logiskai parenkami
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # we start by defining our columns list.
    columns = []
    # then we are going to generate a column for every single column that we have.
    for _ in range(cols):
        # What all this code below is doing. It's picking random values for each row in our column for each value
        # that we're going to have
        # column is equal to empty list
        column = []
# [:] copy! our current_symbols which are the ones we can currently select from, is equal to a copy of all symbols
        current_symbols = all_symbols[:]
        # then we loop through the number of values that we need to generate, which is equal to the number of rows
        # that we have in our slot machine.
        for _ in range(rows):
            # the first value we're going to get here, or a value we're picking is random, not choice (current_symbols)
            value = random.choice(current_symbols)
            # now remove the value, so we don't pick it again, and then we add the value to our column = [] above.
            current_symbols.remove(value)
            # then we add the value to our column.
            column.append(value)
        # we now add our column to our columns = [] list
        columns.append(column)

    return columns

def print_slot_machine(columns): # test the get_slot_machine_spin not in the rows but in columns
    for row in range(len(columns[0])):
        # enumerate gives you the index. So 0,1,2,3 as you loop through as well as the item.
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ") # end= defines how to end the print // defaul end="\n"
            else:
                print(column[row], end="")

        print() # we print for loop for 1 row, and this print brings us to next line, then again for loop prints 1 row


# creating deposit action with description
def deposit():
    while True:  # while loop, and we continue it until break is executed.
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():  # isdigit lets us check if inserted amount is digits. User must only enter numbers
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number!")
    return amount


def get_number_of_lines():  # function to ask on how much lines they want to bet
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # shows valid range from 1 to MAX_LINES entered value (this case = 3)
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # in Python to check if value (lines) is between 2 values
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number!")
    return lines


def get_bet():  # function to ask how much they want to bet on each line
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:  # bet amount must be in MIN_BET(1) and MAX_BET(100) range
                break
            else:
                print(f"Amount must be between {MIN_BET}$ - {MAX_BET}$ ")
        else:
            print("Please enter a number!")
    return amount


def spin(balance):
    lines = get_number_of_lines()  # on how much lines they want to bet
    while True:
        bet = get_bet()
        total_bet = bet * lines  # calculates total_bet by entered amounts.

        if total_bet > balance:  # we must check if total_bet are not exceeding balance
            print(f"You do not have enough to bet that amount, your current balance is: {balance}$")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: {total_bet}$")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}$.")
    print(f"You won on lines:", *winning_lines) # * splat operator
    return winnings - total_bet

def main():
    balance = deposit()  # balance equal to deposit amount
    while True:
        print(f"Current balance is {balance}$")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance}$")

main()
