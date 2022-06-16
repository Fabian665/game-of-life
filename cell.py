class Cell:
    def __init__(self):
        self.alive = False

    def __repr__(self):
        if self.alive:
            return "○"
        return "•"
