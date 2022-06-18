import os
import time
from board import Board


class Game:
    def __init__(self):
        """
        initializes a board and starts the loop
        """
        self.board = None
        self.configurations = {
            1:
                (
                    "Kok's galaxy",
                    (13, 13, False),
                    [
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
                ),
            2:
                (
                    "Glider gun maker",
                    (30, 50, False),
                    [
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
                ),
            3:
                (
                    "simple glider",
                    (10, 10, True),
                    [
                        (7, 1),
                        (8, 2),
                        (9, 0), (9, 1), (9, 2)
                    ]
                )
        }
        choice = self.choose()
        self.play(choice)

    def choose(self):
        """
        prompts the user to choose which configuration to play

        Returns
        -------
        int
            choice number
        """
        print("Which configuration do you want to check out?")
        for index, (name, _, _) in self.configurations.items():
            print(f"{index}. {name}")
        string = f"{list(range(1, len(self.configurations) + 1))}: "
        choice = int(input(string))
        return choice

    def play(self, configuration):
        """
        starts game loop

        Parameters
        ----------
        configuration: int
            which configuration to use

        Returns
        -------
        None
        """
        # Load the configuration
        _, size, cells = self.configurations[configuration]
        board = Board(*size)
        board.flip_cells(cells)

        # Clear the command line and and print the starting board
        os.system('cls' if os.name == 'nt' else 'clear')
        print(board)
        input("Press Enter to start animation")

        # Game loop start
        while True:
            # Clear the command line
            os.system('cls' if os.name == 'nt' else 'clear')
            # Print updated board
            print(board.update())
            print("Press ctrl+c to end")
            time.sleep(0.01)


if __name__ == '__main__':
    game = Game()
