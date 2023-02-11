import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS =3
COLS =3

symbol_count ={
    "🐲" : 2,
    "😎" : 4,
    "🤩"  : 6,
    "✨" : 8
}

symbol_value ={
    "✨" : 5,
    "😎": 4,
    "🤩" : 3,
    "✨" : 2
}

def check_winnings(columns, lines, bet,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]   
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) 
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



def deposit():
    while True:
        amount = input("Enter deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("ERROR! Deposit a value GREATER than zero")
            else:
                break
        else:
            print("ERROR! Enter a number.")
    
    return amount



def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("ERROR! enter a validate number of lines")
        else:
            print("ERROR! please enter a number")
    
    return lines


def get_bet():
    while True:
        amount = input("Enter bet on EACH line?: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Enter a bet between ${MIN_BET} - ${MAX_BET},Thank you")
        else:
            print("ERROR! Enter a number.")
    return amount    

def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"ERROR! Amount exceeds balance.Your current balance is ${balance}")
        else:
            break
    
    print(f"Your are betting ${bet} on {lines} lines.\nTotal bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to spin (q to quit).")
        if spin == "q":
            break
        balance +=game(balance)

    print(f"You're left with ${balance}.Thank You for")

main()