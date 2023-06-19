
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def print_board(self):
        print("------------")
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print("|", end="")
            for cell in row:
                print(f"{cell} |", end="")
            print("\n------------") # reiskia, kad visa cikla perkels i nauja eilute /n new line.

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            # kazkaip cia nusirodo, kad kur zymesim O, tai negalesim zymeti X
        else:
            print("Invalid move, try again!")

    def check_winner(self):
        # apsirasomos pergales kombinacijos , kuomet uzsipildo sie langeliai
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        if " " not in self.board:
            return "Tie!"
        return None

    def play_game(self):
        print("Welcome")
        self.print_board()

        while True:
            position = int(input("player " + self.current_player + " Make your move (0-8): "))
            self.make_move(position)
            self.print_board()


            winner = self.check_winner()
            if winner:
                if winner == "Tie!":
                    print("It's a tie!")
                else:
                    print("Player " + winner + " wins!")
                break

game = TicTacToe()
game.play_game()

