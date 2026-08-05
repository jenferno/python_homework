# Task 6: More on Classes


class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


# Board class for TicTacToe
class Board:

    # Task: Class variables
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    move_map = {
        "upper left": (0, 0),
        "upper center": (0, 1),
        "upper right": (0, 2),
        "middle left": (1, 0),
        "center": (1, 1),
        "middle right": (1, 2),
        "lower left": (2, 0),
        "lower center": (2, 1),
        "lower right": (2, 2)
    }

    # Task: Initialize board
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    # Task: String representation
    def __str__(self):
        rows = []

        for row in self.board_array:
            rows.append(" | ".join(row))

        return "\n-+-+-\n".join(rows)

    # Task: Make a move
    def move(self, move_string):

        if move_string not in self.valid_moves:
            raise TictactoeException("That's not a valid move.")

        row, col = self.move_map[move_string]

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][col] = self.turn
        self.last_move = (row, col)

        # Change player turn
        self.turn = "O" if self.turn == "X" else "X"

    # Task: Check game status
    def whats_next(self):

        lines = []

        # Rows
        lines.extend(self.board_array)

        # Columns
        lines.extend([list(column) for column in zip(*self.board_array)])

        # Diagonals
        lines.append([self.board_array[i][i] for i in range(3)])
        lines.append([self.board_array[i][2 - i] for i in range(3)])

        # Check winner
        for line in lines:
            if line == ["X", "X", "X"]:
                return True, "X has won"

            if line == ["O", "O", "O"]:
                return True, "O has won"

        # Check tie
        if all(
            cell != " "
            for row in self.board_array
            for cell in row
        ):
            return True, "Cat's Game"

        return False, f"{self.turn}'s turn"


# Task: Main game loop
if __name__ == "__main__":

    board = Board()

    print("Welcome to TicTacToe!")

    while True:

        print(board)

        over, status = board.whats_next()

        if over:
            print(status)
            break

        print(f"{board.turn}'s move.")
        print(f"Valid moves: {board.valid_moves}")

        try:
            move = input("Enter your move: ").strip().lower()
            board.move(move)

        except TictactoeException as e:
            print(f"Error: {e.message}")