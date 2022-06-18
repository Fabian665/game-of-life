from cell import Cell


class Board:
    """
    a board for Conway's Game of Life
    """
    def __init__(self, height=35, width=None, wrap=False):
        """
        Initializes a board with turned off cells, if width not specified it defaults to height

        Parameters
        ----------
        wrap
        height: int
        width: int
        """
        self._height = height
        self._width = width if width is not None else height
        self._wrap = wrap
        self._board = [[Cell() for _column in range(self._width)] for _row in range(self._height)]

    def get_cell(self, row_index, col_index):
        """
        Parameters
        ----------
        row_index: int
        col_index: int

        Returns
        -------
        Cell
            the specified cell
        """
        return self._board[row_index][col_index]

    def update(self):
        """
        update the board using Conway's game of life rules:
            1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            2. Any live cell with two or three live neighbours lives on to the next generation.
            3. Any live cell with more than three live neighbours dies, as if by overpopulation.
            4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

        Returns
        -------
        Board
            the updated board
        """
        cells_to_flip = []

        # Loop through the rows and columns
        for row_index in range(self._height):
            for col_index in range(self._width):
                cell_coordinate = (row_index, col_index)  # saving the indices to a variable for readability
                cell = self.get_cell(*cell_coordinate)
                neighbours_sum = self.check_neighbours(*cell_coordinate)
                if cell.is_alive():
                    if neighbours_sum not in range(2, 4):
                        cells_to_flip.append(cell_coordinate)
                else:
                    if neighbours_sum == 3:
                        cells_to_flip.append(cell_coordinate)

        for cell in cells_to_flip:
            self.flip_cell(*cell)

        return self, self._board.copy()

    def check_neighbours(self, row_index, col_index):
        """
        check what is the amount of living neighbors for the cell at (row_index, col_index)

        Parameters
        ----------
        row_index: int
        col_index: int

        Returns
        -------
        int
            the sum of the live neighbours.
        """
        sum_live_neighbours = 0
        for neighbour_row in range(-1, 2):
            for neighbour_column in range(-1, 2):
                if not (neighbour_row == 0 and neighbour_column == 0):  # skip the counting for the piece itself
                    # switch from relative position to absolute
                    (y, x) = (neighbour_row + row_index), (neighbour_column + col_index)

                    # check that the index doesn't exceed the boards limit
                    if self._wrap:
                        y, x = y % self._height, x % self._width
                        sum_live_neighbours += self.get_cell(y, x).is_alive()
                    else:
                        if (0 <= y < self._height) and (0 <= x < self._width):
                            sum_live_neighbours += self.get_cell(y, x).is_alive()

        return sum_live_neighbours

    def cells_generator(self):
        """
        a generator of cells in board. scans each line and returns cells

        Returns
        -------
        iterable
            each element is of type cell
        """
        for y, row in enumerate(self._board):
            for x, cell in enumerate(row):
                yield (y, x), cell

    def flip_cell(self, row, column):
        """
        flips a cell from alive to dead and vice versa

        Parameters
        ----------
        row: int
        column: int

        Returns
        -------
        None
        """
        self._board[row][column].change_state()

    def get_board_list(self):
        return self._board.copy()

    def get_size(self):
        return self._height, self._width

    def flip_cells(self, cells: list):
        """
        flips many cells using flip_cell

        Parameters
        ----------
        cells: array_like
            each element in the array is a tuple of the following form:
            row_index: int, column_index: int

        Returns
        -------
        None
        """
        for cell in cells:
            self.flip_cell(*cell)

    def set_state(self, row_index, column_index, state):
        self.get_cell(row_index=row_index, col_index=column_index).set_state(state)

    def reload(self):
        for row_index, row in enumerate(self._board):
            for column_index, cell in enumerate(row):
                self.set_state(row_index=row_index, column_index=column_index, state=False)

    def change_wrap_setting(self):
        self._wrap = not self._wrap

    def __repr__(self):
        """
        return the string representation of the board

        Returns
        -------
        string
        """
        return "\n".join(' '.join(map(str, row)) for row in self._board)

    def __str__(self):
        """
        return the string representation of the board

        Returns
        -------
        string
        """
        return self.__repr__()
