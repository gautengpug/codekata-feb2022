class Pacman:
    """A class representing a Pacman game.
    The field is alwaysjust 3x3 for now for simplicity.
    """
    def __init__(self):

        self.field = [
            [".", ".", "."],
            [".", "V", "."],
            [".", ".", "."]
        ]
        self.current_row = 1
        self.current_col = 1

    def show(self):
        for row in self.field:
            print(row)
