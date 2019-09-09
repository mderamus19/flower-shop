from flowers import Flower

class Alstroemeria(Flower):
    def __init__(self, color):
        self.color = color
        self.stem_length = 4
        Flower.__init__(self, purple)