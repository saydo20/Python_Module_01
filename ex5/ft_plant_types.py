class Plant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0

    """the setter of the hieght and reject the nigative values"""
    def set_age(self, age_value):
        if age_value < 0:
            print("\nInvalid operation attempted :"
                  f"age {age_value}days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age_value

    """the setter of the age and reject the nigative values"""
    def set_height(self, height_value):
        if height_value < 0:
            print("\nInvalid operation attempted :"
                  f"height {height_value}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height_value

    """create a getter of the height and the getter of the age"""
    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


"""the flower class that inhiret from the Plant class"""


class Flower(Plant):
    def __init__(self, name, color):

        """use the super function to use the parent constructor"""
        super().__init__(name)
        self.color = color

    """the bloom methode that is special for the flower class"""
    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")

    def get_info(self):
        print(f"{self.name} ({__class__.__name__}): {self.get_height()}cm"
              f" {self.get_age()} days, {self.color} color")


"""the tree class that inhiret from the Plant class"""


class Tree(Plant):
    def __init__(self, name, trunk_diameter):
        super().__init__(name)
        self.trunk_diameter = trunk_diameter

    """the produce shade methode for calculate the shade of a tree"""
    def produce_shade(self):
        shade = self.get_height() // self.trunk_diameter + 68
        print(f"{self.name} provides {shade} square meters of shade\n")

    def get_info(self):
        print(f"{self.name} ({__class__.__name__}): {self.get_height()}cm"
              f" {self.get_age()} days, {self.trunk_diameter}cm diameter")


"""the Vegetable class that inhiret from the Plant class"""


class Vegetable(Plant):
    def __init__(self, name, harvest_season):
        super().__init__(name)
        self.harvest_season = harvest_season
    """check the season of the harvest and the print what it rich"""
    def nutritional_value(self):
        if self.harvest_season == "summer harvest":
            print(f"{self.name} is rich in vitamin C")
        elif self.harvest_season == "winter harvest":
            print(f"{self.name} is rich in vitamin A")
        elif self.harvest_season == "spring harvest":
            print(f"{self.name} is rich in iron")
        elif self.harvest_season == "autumn harvest":
            print(f"{self.name} is rich in potassium")
        else:
            print(f"{self.name} is rich in nutrients")

    def get_info(self):
        print(f"{self.name} ({__class__.__name__}): {self.get_height()}cm"
              f" {self.get_age()} days, {self.harvest_season}")


if __name__ == "__main__":
    tulip = Flower("Tulip", "pink")
    tulip.set_height(15)
    tulip.set_age(40)
    rose = Flower("Rose", "red")
    rose.set_height(25)
    rose.set_age(30)
    oak = Tree("Oak", 50)
    oak.set_height(500)
    oak.set_age(1825)
    palm = Tree("Palm", 30)
    palm.set_height(1000)
    palm.set_age(800)
    tomato = Vegetable("Tomato", "summer harvest")
    tomato.set_height(80)
    tomato.set_age(90)
    carrot = Vegetable("Carrot", "winter")
    carrot.set_height(120)
    carrot.set_age(30)
    print("=== Garden Plant Types ===\n")
    rose.get_info()
    rose.bloom()
    oak.get_info()
    oak.produce_shade()
    tomato.get_info()
    tomato.nutritional_value()
