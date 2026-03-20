import random
from colorama import init, Fore, Style
init(autoreset=True)
# =========================================
# CONSTANTS (DO NOT EDIT)
# =========================================
win_conditions = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def display_board(board):
    """Prints the Tic-Tac-Toe board in color."""
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    """Asks player to choose X or O and returns (player_symbol, ai_symbol)."""
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).strip().upper()
    return ('X', 'O') if symbol == 'X' else ('O', 'X')

# ==========================================================
# TODO 1: player_move(board, symbol)
# ==========================================================
def player_move(board, symbol):
    move= -1
    while move not in range(1,10) or not board[move - 1]. isdigit():
        try:
            move= int(input("Enter your move(1-9:)")) 
            if move not in range (1-10) or not board[move-1].isdigit():
                print("invalid move. Please try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
            board[move -1]= symbol

    
         

# ==========================================================
# TODO 2: ai_move(board, ai_symbol, player_symbol)
# ==========================================================
def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i]=ai_symbol
            if check_win(board_copy,ai_symbol):
                board[i] =ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i]=player_symbol
            if check_win(board_copy,player_symbol):
                board[i] =ai_symbol
                return
    possible_moves = [i for i in range (9)if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

# ==========================================================
# TODO 3: check_win(board, symbol)
# ==========================================================
def check_win(board, symbol):
    win_conditions =  [
        (0,1,2),(3,4,5),(6,7,8), #horizontal
        (0,3,6),(1,4,7),(2,5,8), #vertical
        (0,4,8),(2,4,6) #diagonal
        ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

# ==========================================================
# TODO 4: check_full(board)
# ==========================================================
def check_full(board):
    return all(not spot.isdigit() for spot in board)
    

# ==========================================================
# MAIN GAME (NOW WITH A FEW TODOs)
# ==========================================================
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name =input(Fore.GREEN + "Enter your name" + Style.RESET_ALL)

    while True:
       board = ['1','2','3','4','5','6','7','8','9']
       player_symbol, ai_symbol = player_choice()
       turn = 'player'
       game_on = True

        

    
    while game_on:
            display_board(board)


            if turn == "Player":
                diplay_board(board)
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print("Congrats!" + player_name + ", you have won the game!")
                    game_one= False
                else:
                    if check_win(board):
                        display_board(board)
                        print("it is a tie!")
                        break
                    else:
                        turn= 'Ai'
            else:
                ai_move(board,ai_symbol,player_symbol)
                if check_win(board,ai_symbol):
                    display_board(board)
                    print("Ai has won the game!")
                    game_on = False
                else:
                    if check_ful(board):
                        display_board(board)
                        print("its a tie!")
                        break
                    else: 
                        turn = 'player'
    play_again= input("Do you want to play this game again?(yes/no:)")
    if play_again != 'yes':
            print("Thank you for playing")
            
            
    
                
if __name__ == "__main__":
    tic_tac_toe()