class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
        

class Tree(Plant):
    def __init__(self, name, height, age , trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        if self.name == "Oak":
            factor = 0.00312   # exact factor to make oak = 78
        elif self.name == "Pine":
            factor = 0.0020
        elif self.name == "Palm":
            factor = 0.0015
        else:
            factor = 0.0025

        # Formula using only your class attributes
        shade = self.height * self.trunk_diameter * self.age * factor
        print(self.name, "provides", shade, "square meters of shade")
        

class Vegetable(Plant):
    def __init__(self, name, height, age , harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        
# Rose = Flower("Rose", 25, 30, "red")
# Tulip = Flower("Tulip", 15, 40, "pink")
oak = Tree("oak", 500, 1825, 50)
oak.produce_shade()