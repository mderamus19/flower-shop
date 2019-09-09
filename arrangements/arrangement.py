class Arrangement:
    def __init__(self):
        self.__flowers = []

    def enhance(self, flower):
        self.__flowers.append(flower)

    def __str__(self):
        return(f"{self.flowers}")
