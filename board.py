from cell import Cell


class Board:
    def __init__(self, size=35):
        self._size = size
        self._board = [[Cell() for _index in range(size)] for _index in range(size)]

    def update(self):
        for row_index in range(self._size):
            for col_index in range(self._size):
                print(self.check_neighbours(row_index, col_index))

    def check_neighbours(self, row_index, col_index):
        sum_live_neighbours = 0
        for neighbour_row in range(-1, 2):
            for neighbour_column in range(-1, 2):
                if not (neighbour_row == 0 and neighbour_column == 0):
                    neighbour_row_copy, neighbour_column = (neighbour_row + row_index), (neighbour_column + col_index)

                    if (0 <= neighbour_row_copy < (self._size - 1)) and (0 <= neighbour_column < (self._size - 1)):
                        sum_live_neighbours += self._board[neighbour_row_copy][neighbour_column].is_alive()

        return sum_live_neighbours

    def cells_generator(self):
        for row in self._board:
            for cell in row:
                yield cell

    def set_board(self):
        self._board[1][1].change_state()

    def __repr__(self):
        return "\n".join(' '.join(map(str, row)) for row in self._board)
