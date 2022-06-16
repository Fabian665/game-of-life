from cell import Cell


class Board:
    def __init__(self, size=35):
        self._board = [[Cell() for _index in range(size)] for _index in range(size)]

    def update(self):
        pass

    def check_neighbours(self, row, column):
        sum_of_live_neighbours = 0
        for neighbour_row in range(-1, 2):
            for neighbour_column in range(-1, 2):
                sum_of_live_neighbours += self._board[neighbour_row + row][neighbour_column + column].is_alive()
        return sum_of_live_neighbours

    def cells_generator(self):
        for row in self._board:
            for cell in row:
                yield cell

    def set_board(self):
        self._board[1][1].change_state()

    def __repr__(self):
        return "\n".join(' '.join(map(str, row)) for row in self._board)
