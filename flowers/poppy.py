from flowers import Flower
from flowers import Organic

class Poppy(Flower, Organic):
    def __init__(self):
        self.stem_length = 4
        Organic.__init__(self)
        Flower.__init__(self, "orange")