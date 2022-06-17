from unittest import TestCase
from board import Board


class BoardTest(TestCase):
    def test_update(self):
        board = Board(3)
        try:
            board.update()
        except IndexError:
            self.fail("update went out of bounds")

        for _, cell in board.cells_generator():
            self.assertFalse(cell.is_alive())

        board.flip_cell(1, 1)
        board.update()

        for _, cell in board.cells_generator():
            self.assertFalse(cell.is_alive())

        board = Board(3)
        board.flip_cell(0, 1)
        board.flip_cell(0, 2)
        board.flip_cell(1, 2)
        board.update()

        for index, (_, cell) in enumerate(board.cells_generator()):
            if index == 1 or index == 2 or index == 4 or index == 5:
                self.assertTrue(cell.is_alive(), f"Cell no. {index}, should be True")
            else:
                self.assertFalse(cell.is_alive(), f"Cell no. {index}, should be False")

        board = Board(3)
        board.flip_cell(1, 0)
        board.flip_cell(1, 1)
        board.flip_cell(1, 2)
        board.update()

        for index, (_, cell) in enumerate(board.cells_generator()):
            if index == 1 or index == 4 or index == 7:
                self.assertTrue(cell.is_alive(), f"Cell no. {index}, should be True")
            else:
                self.assertFalse(cell.is_alive(), f"Cell no. {index}, should be False")

        board.update()

        for index, (_, cell) in enumerate(board.cells_generator()):
            if index == 3 or index == 4 or index == 5:
                self.assertTrue(cell.is_alive(), f"Cell no. {index}, should be True")
            else:
                self.assertFalse(cell.is_alive(), f"Cell no. {index}, should be False")

    def test_check_neighbours(self):
        board = Board(3)
        middle = (1, 1)
        cell = board.check_neighbours(*middle)
        expected_result = 0
        self.assertEqual(cell, expected_result, f"{middle} neighbour sum should be {expected_result} but is {cell}")

        board.flip_cell(1, 1)

        cell = board.check_neighbours(*middle)
        expected_result = 0
        self.assertEqual(cell, expected_result, f"{middle} neighbour sum should be {expected_result} but is {cell}")

        top_left = (0, 0)
        cell = board.check_neighbours(*top_left)
        expected_result = 1
        self.assertEqual(cell, expected_result, f"{top_left} neighbour sum should be {expected_result} but is {cell}")

        top_right = (0, 2)
        try:
            cell = board.check_neighbours(*top_right)
        except IndexError:
            self.fail("check neighbours went out of bounds")
        else:
            expected_result = 1
            self.assertEqual(cell, expected_result, f"{top_right} neighbour sum should be {expected_result} but"
                                                    f" is {cell}")

    def test_flip_cell(self):
        board = Board(3)
        first_cell = (0, 0)
        board.flip_cell(*first_cell)
        self.assertTrue(board.get_cell(*first_cell).is_alive(), f"cell {first_cell} should be True")

        board.flip_cell(*first_cell)
        self.assertFalse(board.get_cell(*first_cell).is_alive(), f"cell {first_cell} should be False")

        last_cell = (2, 2)
        board.flip_cell(*last_cell)
        self.assertTrue(board.get_cell(*last_cell).is_alive(), f"cell {last_cell} should be True")

        a_cell = (0, 2)
        board.flip_cell(*a_cell)
        self.assertTrue(board.get_cell(*a_cell).is_alive(), f"cell {a_cell} should be True")

        a_cell = (2, 0)
        board.flip_cell(*a_cell)
        self.assertTrue(board.get_cell(*a_cell).is_alive(), f"cell {a_cell} should be True")

    def test_koks_galaxy(self):
        board = Board(13)
        cells = [
            (2, 2), (2, 3), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
            (3, 2), (3, 3), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
            (4, 2), (4, 3),
            (5, 2), (5, 3), (5, 9), (5, 10),
            (6, 2), (6, 3), (6, 9), (6, 10),
            (7, 2), (7, 3), (7, 9), (7, 10),
            (8, 9), (8, 10),
            (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 9), (9, 10),
            (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 9), (10, 10)
        ]

        board.flip_cells(cells)

        for i in range(8):
            board.update()

        for cell in cells:
            self.assertTrue(board.get_cell(*cell).is_alive(), f"cell {cell} should be True")

    def test_glider_gun_maker(self):
        board = Board(40, 43)
        cells = [
            (2, 35),
            (3, 35), (3, 37),
            (4, 1), (4, 23), (4, 25), (4, 35), (4, 36),
            (5, 1), (5, 3), (5, 23), (5, 24),
            (6, 1), (6, 2), (6, 9), (6, 11), (6, 24), (6, 37), (6, 38), (6, 39),
            (7, 9), (7, 10), (7, 37),
            (8, 3), (8, 4), (8, 5), (8, 10), (8, 24), (8, 25), (8, 38),
            (9, 3), (9, 24), (9, 26), (9, 30),
            (10, 4), (10, 10), (10, 11), (10, 24), (10, 29), (10, 30),
            (11, 10), (11, 12), (11, 16), (11, 29), (11, 31),
            (12, 10), (12, 15), (12, 16), (12, 21), (12, 22),
            (13, 15), (13, 17), (13, 21), (13, 23),
            (14, 21),
            (15, 40), (15, 41),
            (16, 40), (16, 42),
            (17, 40),
            (20, 29), (20, 30), (20, 31),
            (21, 29),
            (22, 30)
        ]

        board.flip_cells(cells)

        for i in range(100):
            try:
                board.update()
            except IndexError:
                self.fail("IndexError occurred")

    def test_simple_glider(self):
        board = Board(10, wrap=True)
        cells = [
            (7, 1),
            (8, 2),
            (9, 0), (9, 1), (9, 2)
        ]

        board.flip_cells(cells)

        for i in range(32):
            board.update()

        for coordinate, cell in board.cells_generator():
            if coordinate in {(5, 9), (6, 0), (7, 0), (7, 8), (7, 9)}:
                self.assertTrue(cell.is_alive(), f"cell in {coordinate} should be alive")
            else:
                self.assertFalse(cell.is_alive(), f"cell in {coordinate} should be dead")
