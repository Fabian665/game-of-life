from unittest import TestCase
from board import Board


class BoardTest(TestCase):
    def test_update(self):
        board = Board(3)
        try:
            board.update()
        except IndexError:
            self.fail("update went out of bounds")

        for cell in board.cells_generator():
            self.assertFalse(cell.is_alive())

        board.flip_cell(1, 1)
        board.update()

        for index, cell in enumerate(board.cells_generator()):
            self.assertFalse(cell.is_alive())

        board = Board(3)
        board.flip_cell(0, 1)
        board.flip_cell(0, 2)
        board.flip_cell(1, 2)
        board.update()

        for index, cell in enumerate(board.cells_generator()):
            if index == 1 or index == 2 or index == 4 or index == 5:
                self.assertTrue(cell.is_alive(), f"Cell no. {index}, should be True")
            else:
                self.assertFalse(cell.is_alive(), f"Cell no. {index}, should be False")

        board = Board(3)
        board.flip_cell(1, 0)
        board.flip_cell(1, 1)
        board.flip_cell(1, 2)
        board.update()

        for index, cell in enumerate(board.cells_generator()):
            if index == 1 or index == 4 or index == 7:
                self.assertTrue(cell.is_alive(), f"Cell no. {index}, should be True")
            else:
                self.assertFalse(cell.is_alive(), f"Cell no. {index}, should be False")

        board.update()

        for index, cell in enumerate(board.cells_generator()):
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
            (2, 2), (2, 3),     (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
            (3, 2), (3, 3),     (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
            (4, 2), (4, 3),
            (5, 2), (5, 3),                                     (5, 9), (5, 10),
            (6, 2), (6, 3),                                     (6, 9), (6, 10),
            (7, 2), (7, 3),                                     (7, 9), (7, 10),
                                                                (8, 9), (8, 10),
            (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7),     (9, 9), (9, 10),
            (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7),     (10, 9), (10, 10)
        ]

        board.flip_cells(cells)

        for i in range(8):
            board.update()

        for cell in cells:
            self.assertTrue(board.get_cell(*cell).is_alive(), f"cell {cell} should be True")
