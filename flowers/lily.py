from flowers import Flower
from flowers import Organic
class Lily(Flower, Organic):
    def __init__(self):
        self.organic = False
        Flower.__init__(self, "pink")
        Organic.__init__(self)