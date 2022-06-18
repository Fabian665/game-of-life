class Cell:
    """
    a cell in Conway's Game of Life
    """
    def __init__(self):
        """
        initializes a dead cell
        """
        self._alive = False

    def is_alive(self):
        """
        Returns
        -------
        bool
            True if cell is alive else False
        """
        return self._alive

    def change_state(self):
        """
        Changes the state of the cell from alive to dead and vice versa
        """
        self._alive = not self._alive

    def set_state(self, state):
        self._alive = state

    def __repr__(self):
        """
        Returns
        -------
        string
            representation of the cell
        """
        if self._alive:
            return "■"
        return " "
