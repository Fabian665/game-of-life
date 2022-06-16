from unittest import TestCase
from board import Board


class BoardTest(TestCase):
    def test_update(self):
        board = Board(3)
        try:
            board.update()
        except IndexError:
            self.fail("update went out of bounds")

    def test_check_neighbours(self):
        board = Board(3)
        middle = (1, 1)
        cell = board.check_neighbours(*middle)
        expected_result = 0
        self.assertEqual(cell, expected_result, f"{middle} neighbour sum should be {expected_result} but is {cell}")

        board.set_board()

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
            self.assertEqual(cell, expected_result, f"{top_right} neighbour sum should be {expected_result} but is {cell}")


    def test_cells_generator(self):
        assert True

    def test_set_board(self):
        assert True
