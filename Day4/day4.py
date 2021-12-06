import re


class Square:
    """
    This class creates an individual square on a Bingo Board
    """

    def __init__(self, value):
        self.value = value
        self.marked = False


class Row:
    """
    This class creates a row on a Bingo Board
    """

    def __init__(self, values):
        self.squares = []
        self.length = 0
        for i in values:
            self.squares.append(Square(i))
            self.length += 1

    def get_at_index(self, index):
        """Getter method"""
        return self.squares[index]

    def __getitem__(self, index):
        """Same functionality as get_at_index() method above, but called using array[index] syntax"""
        return self.get_at_index(index)


class Board:
    """
    This class creates a Bingo Board object
    """

    def __init__(self):
        self.rows = []
        self.marked_sum = 0
        self.unmarked_sum = 0
        self.bingo = False

    def add_row(self, array):
        """This adds a row to the Bingo Boad"""
        self.rows.append(Row(array))
        for i in range(len(array)):
            self.unmarked_sum += array[i]

    def mark_number(self, value):
        """This checks if the a number is on the Bingo Board. If so, it marks the number and calls check_bingo"""
        for i in range(len(self.rows)):
            for j in range(self.rows[i].length):
                if self.rows[i][j].value == value:
                    self.rows[i][j].marked = True
                    self.marked_sum += self.rows[i][j].value
                    self.unmarked_sum -= self.rows[i][j].value
                    self.check_bingo(value)

    def check_bingo(self, last_number):
        """This checks if the recently marked number causes a BINGO!!!"""
        for i in range(len(self.rows)):
            marks = 0
            for j in range(self.rows[i].length):
                if self.rows[i][j].marked:
                    marks += 1
                    # Check for horizontal BINGO!!!
                    if marks == self.rows[i].length and not self.bingo:
                        print("BINGO!!!!   Score: ", self.unmarked_sum * last_number)
                        self.bingo = True
                    elif i == 0:
                        vert_marks = 1
                        # Check for vertical BINGO!!!
                        for k in range(1, len(self.rows)):
                            if self.rows[k][j].marked:
                                vert_marks += 1
                        if vert_marks == len(self.rows) and not self.bingo:
                            print("BINGO!!!!   Score: ", self.unmarked_sum * last_number)
                            self.bingo = True


with open("input.txt") as input_file:
    raw_data = re.split('\n+', input_file.read())

    # Pull out the bingo numbers to be called
    numbers = list(map(int, re.findall('\d+', raw_data[0])))

    # Create an array of arrays, each containing a row of a box
    box_rows = []
    for i in range(1, len(raw_data) - 1):
        box_rows.append(list(map(int, re.findall('\d+', raw_data[i]))))

board_bag = []

new_board = Board()

# Create all the boards
for i in range(len(box_rows)):
    if i % 5 == 0:
        board_bag.append(new_board)
        new_board = Board()
    new_board.add_row(box_rows[i])

# Because the first time the above loop runs, an empty board is added to the bag
del board_bag[0]

# Start calling numbers, it's time to play!
for i in range(len(numbers)):
    for j in range(len(board_bag)):
        board_bag[j].mark_number(numbers[i])
