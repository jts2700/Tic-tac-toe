def print_board(board):
    """Print the current state of the board"""
    print("\n   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   \n")

def check_winner(board):
    """Check if there's a winner"""
    # Winning combinations (indices)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    return None

def is_board_full(board):
    """Check if the board is full"""
    return ' ' not in board

def get_player_move(board, player):
    """Get a valid move from the player"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move! Please choose an empty spot (1-9).")
        except ValueError:
            print("Please enter a valid number (1-9).")

def play_tic_tac_toe():
    """Main game function"""
    # Initialize empty board
    board = [' '] * 9
    current_player = 'X'
    
    print("Welcome to Tic Tac Toe!")
    print("Board positions are numbered 1-9:")
    print("\n 1 | 2 | 3 ")
    print("___|___|___")
    print(" 4 | 5 | 6 ")
    print("___|___|___")
    print(" 7 | 8 | 9 ")
    print("\n")
    
    # Game loop
    while True:
        print_board(board)
        
        # Get player move
        move = get_player_move(board, current_player)
        board[move] = current_player
        
        # Check for winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break
        
        # Check for tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    
    # Ask if players want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_tic_tac_toe()
    else:
        print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_tic_tac_toe()