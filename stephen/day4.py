import sys


class Bingoboard:
    def __init__(self, id):
        self.id = id
        self.board = []
        self.called_numbers = []
        self.is_winner = False
        for _ in range(5):
            self.called_numbers.append([False, False, False, False, False])

    def add_row(self, row):
        self.board.append(row)

    def call_number(self, number):
        for row_idx in range(len(self.board)):
            for col_idx in range(len(self.board[0])):
                if self.board[row_idx][col_idx] == number:
                    self.called_numbers[row_idx][col_idx] = True
                    #print(f"  {number} was found in board {self.id} ({row_idx}, {col_idx})")

    def check_if_winner(self):
        #check all rows:
        for row_idx, row in enumerate(self.called_numbers):
            if all(row):
                #print(f"Winner has been found (board {self.id}, row {row_idx})")
                self.is_winner = True
                return True

        for col_idx in range(len(self.called_numbers[0])):
            column = [self.called_numbers[row_idx][col_idx] for row_idx in range(len(self.called_numbers))]
            if all(column):
                #print(f"Winner has been found (board {self.id}, column {col_idx})")
                self.is_winner = True
                return True

        return False

    def print_called_numbers(self):
        for row_idx in range(len(self.called_numbers)):
            for col_idx in range(len(self.called_numbers[0])):
                print(self.called_numbers[row_idx][col_idx], end=" ")
            print()
        print()

    def calculate_win(self, last_called_number):
        uncalled_sum = 0
        for row_idx in range(len(self.called_numbers)):
            for col_idx in range(len(self.called_numbers[row_idx])):
                if not self.called_numbers[row_idx][col_idx]:
                    uncalled_sum += self.board[row_idx][col_idx]

        return uncalled_sum  * last_called_number

    def __repr__(self):
        board_layout = "\n"
        for row in self.board:
            for number in row:
                board_layout+= f"{number:2} "
            board_layout += "\n"
        board_layout += "\n"
        return board_layout[:-1] #remove excess \n at end

def process_input(filename):
    numbers_called = None
    bingo_boards = []
    id_counter = 1
    new_bingo_board = Bingoboard(id_counter)
    with open(filename) as f:
        lines = f.readlines()
        numbers_called = [int(x.strip()) for x in lines[0].split(",")]
        for line in lines[2:]:
            if line == "\n":
                bingo_boards.append(new_bingo_board)
                id_counter += 1
                new_bingo_board = Bingoboard(id_counter)
                continue
                #return numbers_called, bingo_boards
            bingo_board_row = []
            for number in line.split(" "):
                if number != "":
                    bingo_board_row.append(int(number.strip()))
            new_bingo_board.add_row(bingo_board_row)

    #print(numbers_called)
    return numbers_called, bingo_boards



def part1():
    numbers_called, bingo_boards  = process_input("day4-input.txt")
    for number in numbers_called:
        #print(f"Calling number {number}")
        for board in bingo_boards:
            board.call_number(number)
            if board.check_if_winner():
                #print(board)
                final_score = board.calculate_win(number)
                print(f"First board to win is board {board.id}, with a final called number of {number}")
                print(f"Final score of first board to win is {final_score}")
                return


def part2():
    numbers_called, bingo_boards  = process_input("day4-input.txt")
    already_winners = [] # list of ids of boards that have already won
    called_numbers = []
    for number in numbers_called:
        if len(already_winners) == len(bingo_boards):
            break # all boards have won, so we can stop
        #print(f"Calling number {number}")
        called_numbers.append(number)
        for board in bingo_boards:
            if board.id not in already_winners:
                board.call_number(number)
                if board.check_if_winner():
                    #print(f"Board {board.id} is a winner!")
                    already_winners.append(board.id)

    last_winner = already_winners[-1]
    last_called_number = called_numbers[-1]
    for board in bingo_boards:
        if board.id == last_winner:
            print(f"Last board to win is board {board.id}, with final called number of {last_called_number}")
            print(f"Final score of last board to win is {board.calculate_win(last_called_number)}")


if __name__ == '__main__':
    part1()
    print()
    part2()