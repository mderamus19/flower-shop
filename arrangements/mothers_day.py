from . import Arrangement

class MothersDay(Arrangement):
    def __init__(self):
        super().__init__()

#Override the 'enhance' method to ensure only
#roses, lillies, and alstroemeria can be added
def enhance(self, flower):
        try:
            if flower.organic == True:
                self.__flowers.append(flower)
        except AttributeError:
            print(f'You can only add organic flowers')


