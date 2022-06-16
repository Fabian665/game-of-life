from cell import Cell


class Board:
    def __init__(self, width=35, height=None):
        self._width = width
        self._height = width if height is None else height
        self._board = [[Cell() for _index in range(self._width)] for _index in range(self._height)]

    def get_cell(self, row_index: int, col_index: int) -> Cell:
        return self._board[row_index][col_index]

    def update(self):
        cells_to_flip = []
        for row_index in range(self._width):
            for col_index in range(self._height):
                cell_coordinate = (row_index, col_index)
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

        return self

    def check_neighbours(self, row_index: int, col_index: int) -> int:
        sum_live_neighbours = 0
        for neighbour_row in range(-1, 2):
            for neighbour_column in range(-1, 2):
                if not (neighbour_row == 0 and neighbour_column == 0):
                    neighbour_row_copy, neighbour_column = (neighbour_row + row_index), (neighbour_column + col_index)

                    if (0 <= neighbour_row_copy < self._height) and (0 <= neighbour_column < self._width):
                        sum_live_neighbours += self._board[neighbour_row_copy][neighbour_column].is_alive()

        return sum_live_neighbours

    def cells_generator(self):
        for row in self._board:
            for cell in row:
                yield cell

    def flip_cell(self, row: int, column: int) -> None:
        self._board[row][column].change_state()

    def flip_cells(self, cells: list) -> None:
        for cell in cells:
            self.flip_cell(*cell)

    def __repr__(self):
        return "\n".join(' '.join(map(str, row)) for row in self._board)

    def __str__(self):
        return self.__repr__()
