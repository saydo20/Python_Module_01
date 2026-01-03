class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        # print(f"Plant created: {self.name}")
    """the setter of the hieght and reject the nigative values"""
    def set_hieght(self, age_value):
        if age_value < 0:
            print()
            print("Invalid operation attempted :"
                  f"age {age_value}days [REJECTED]")
            print("Security: Negative age rejected")
            print()
        else:
            self._age = age_value
            print(f"Age updated: {self._height}days [OK]")
    """the setter of the age and reject the nigative values"""
    def set_age(self, height_value):
        if height_value < 0:
            print()
            print("Invalid operation attempted :"
                  f"age {height_value}days [REJECTED]")
            print("Security: Negative height rejected")
            print()
        else:
            self._height = height_value
            print(f"Height updated: {self._height}cm [OK]")
    """create a getter of the height and the getter of the age"""
    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


class Flower(Plant):
    def __init__(self, name, _height, _age, color):
        super().__init__(name, _height, _age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")
        print()

    def get_info(self):
        print(f"{self.name} ({__class__.__name__}): {self.get_height()}cm"
              f" {self.get_age()} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name, _height, _age, trunk_diameter):
        super().__init__(name, _height, _age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        num = int(self.get_height()) // 100
        print(f"Oak provides {int(3.141592653589793 * (num**2))}"
              " square meters of shade")
        print()

    def get_info(self):
        print(f"{self.name} ({__class__.__name__}): {self.get_height()}cm"
              f" {self.get_age()} days, {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name, _height, _age, harvest_season):
        super().__init__(name, _height, _age)
        self.harvest_season = harvest_season

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


Tulip = Flower("Tulip", 15, 40, "pink")
Rose = Flower("Rose", 25, 30, "red")
Oak = Tree("Oak", 500, 1825, 50)
Oalm = Tree("Palm", 1000, 800, 30)
Tomato = Vegetable("Tomato", 80, 90, "summer harvest")
Carrot = Vegetable("Carrot", 120, 30, "winter")
print("=== Garden Plant Types ===")
print()
Rose.get_info()
Rose.bloom()
Oak.get_info()
Oak.produce_shade()
Tomato.get_info()
Tomato.nutritional_value()
