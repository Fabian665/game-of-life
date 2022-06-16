class Cell:
    def __init__(self):
        self._alive = False

    def is_alive(self):
        return self._alive

    def change_state(self):
        self._alive = not self._alive

    def __repr__(self):
        if self._alive:
            return "○"
        return "•"
