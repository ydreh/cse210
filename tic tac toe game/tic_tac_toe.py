#Tic-Tac_Toe Game Assignment
#Author: Herdy Rodriguez

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        print_board(board)
        make_move(player, board)
        player = next_player(player)
    print_board(board)
    print("Good game. Thanks for playing!") 

def create_board():
    board = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
    return board

def print_board(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    move = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[move - 1] = player

    

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()