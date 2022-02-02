class Pacman:
    """A class representing a Pacman game.
    The field is alwaysjust 3x3 for now for simplicity.
    """
    def __init__(self):

        self.pacman = 'V'
        self.direction = 'up'
        self.field = [
            [".", ".", "."],
            [".", self.pacman, "."],
            [".", ".", "."]
        ]
        self.current_row = 1
        self.current_col = 1

    def show(self):
        for row in self.field:
            print(row)

    def is_coords_in_range(self, row: int, col: int) -> bool:
        """Check if the given row and colum coordinates are valid."""
        max_row = len(self.field) - 1
        max_col = len(self.field[0]) - 1
        if row < 0 or row > max_row:
            return False
        if col < 0 or col > max_col:
            return False
        return True

    def rotate(self, direction):
        orientation = {'up': 'v', 'left': '>', 'right': '<', 'down': '^'}
        
        if direction in orientation:
            self.direction = direction
            self.pacman = orientation[direction]
            current_list = self.field[self.current_row]
            current_list[self.current_col] = self.pacman
        else:
            raise ValueError('invalid direction')

    def move(self):
        ok = False
        old_row = self.current_row
        old_col = self.current_col

        if self.direction == 'up':
            if self.is_coords_in_range(self.current_row-1, self.current_col):
                self.current_row -= 1
                ok = True
        elif self.direction == 'down':
            if self.is_coords_in_range(self.current_row+1, self.current_col):
                self.current_row += 1
                ok = True
        elif self.direction == 'left':
            if self.is_coords_in_range(self.current_row, self.current_col-1):
                self.current_col -= 1
                ok = True
        elif self.direction == 'right':
            if self.is_coords_in_range(self.current_row, self.current_col+1):
                self.current_col += 1
                ok = True

        if not ok:
            raise ValueError('invalid move')            

        self.field[old_row][old_col] = ' '
        self.field[self.current_row][self.current_col] = self.pacman
    