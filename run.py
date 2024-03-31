from random import randint

user = []
user_guesses = []
comp = []


def make_board(board):
    for i in range(5):
        board.append([" X "]*5)
    return board


def print_board(board):
    for ind in board:
        print(" ".join(ind))


def random_num(board):
    return randint(0, len(board)-1)


def generate_ship_loc(board):
    ship_num = 0
    while ship_num < 4:
        ship_num = 0
        ship_col = random_num(board)
        ship_row = random_num(board)
        board[ship_row][ship_col] = " o "
        for row in board:
            ship_num += row.count(" o ")


def welcome():
    print("Welcome to Battleship Bandits!")
    username = input("Please enter a username: \n")
    print(f'\nHi {username}! Lets begin the game.'
          ' First to sink all 4 of the opponents battleships will win.')
    print('\nX = Not guessed, * = Missed location # = Hit Battleship'
          ' - 5 x 5 Board, Make your guess in the range of 1 to 5')


def generate_boards():
    make_board(user)
    make_board(comp)
    make_board(user_guesses)
    generate_ship_loc(user)
    generate_ship_loc(comp)


def user_guess():
    print("Computers Board:")
    print_board(user_guesses)
    repeat = True
    while repeat:
        while True:
            print("\nGuess Column")
            guess_col = input("Enter a number and press enter: \n")
            if validate_data(guess_col):
                break
        while True:
            print("\nGuess Row")
            guess_row = input("Enter a number and press enter: \n")
            if validate_data(guess_row):
                break

        guess_col = int(guess_col)-1
        guess_row = int(guess_row)-1

        if (user_guesses[guess_row][guess_col] == " * " or
                user_guesses[guess_row][guess_col] == " # "):
            print("You've guessed this location already!")
        else:
            repeat = False
    if comp[guess_row][guess_col] == " o ":
        user_guesses[guess_row][guess_col] = " # "
        print("\nNice! You sunk their ship.")
    else:
        user_guesses[guess_row][guess_col] = " * "
        print("\nYou missed the ship. :(")


def comp_guess():
    print("\n\nComputer's Turn.")
    repeat = True
    guess_col = random_num(comp)
    guess_row = random_num(comp)
    while repeat:
        if (user[guess_row][guess_col] == " * " or
                user[guess_row][guess_col] == " # "):
            guess_col = random_num(comp)
            guess_row = random_num(comp)
        else:
            repeat = False
    print(f"Computer guessed {guess_col + 1}, {guess_row + 1}")
    if user[guess_row][guess_col] == " o ":
        user[guess_row][guess_col] = " # "
        print("Battleship has been sunk! :(")
    else:
        user[guess_row][guess_col] = " * "
        print("Computer missed.")


def game_play():
    generate_boards()
    welcome()
    i = 0
    while i < 10:
        print(f"\nTurn: {i +1}/10 \n")
        user_guess()
        print_board(user_guesses)
        input("\nPress Enter to continue...")
        comp_guess()
        print("\nYour Board: ")
        print_board(user)
        input("\nPress Enter to continue...")
        i += 1
        if check_winner(user) == 4:
            i = 10
        elif check_winner(user_guesses) == 4:
            i = 10
    check_winner_final()


def validate_data(value):
    try:
        if int(value) > 5 or int(value) < 1:
            raise ValueError(
                "Please guess within the range of 1 to 5"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        print("Please guess numbers only")
        return False
    return True


def check_winner(board):
    total = 0
    for list in board:
        total += list.count(" # ")
    return total


def check_winner_final():
    user_result = check_winner(user_guesses)
    comp_result = check_winner(user)
    if user_result > comp_result:
        print("Congratulations! You win!")
    elif user_result < comp_result:
        print("Computer wins this time.. try again!")
    else:
        print("Looks like its a tie.")


game_play()
