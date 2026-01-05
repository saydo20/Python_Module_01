class GardenManager:
    def __init__(self, name):
        self.name = name

    class GardenStats:
        def __init__(self):
            self.Gardens = []

        def add_garden(self):
            Garden_name = input("what is the name of the gareden: ")
            self.Gardens = self.Gardens + [Garden_name]
            print(f"the garden {Garden_name} is added")

    @classmethod
    def create_garden_network():
        pass


class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def set_age(self, age_value):
        if age_value < 0:
            print("Invalid operation attemped"
                  f"age {age_value}days [REJECTED]")
        else:
            self._age = age_value
            print(f"Age updated: {self._age}days [OK]")

    def set_height(self, height_value):
        if height_value < 0:
            print("Invalid operation attemped"
                  f"height {height_value}cm [REJECTED]")
        else:
            self._height = height_value
            print(f"Height updated: {self._height}")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, Prize_points):
        super().__init__(name, height, age, color)
        self.Prize_points = Prize_points


class Garden:
    def __init__(self, garden_name):
        self.garden_name = garden_name
        self.plants = []

    def add_plant(self, plant):
        self.plants = self.plants + [plant]
