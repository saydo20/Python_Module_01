class GardenManager:
    def __init__(self, name):
        self.name = name
        self.stats = self.GardenStats()
        self.ManagerGardens = []

    class GardenStats:
        def __init__(self):
            self.Gardens = []

        def add_garden(self, garden):
            self.Gardens = self.Gardens + [garden]

    def add_garden(self, garden):
        self.ManagerGardens = self.ManagerGardens + [garden]
        self.stats.add_garden(garden)

    def show_garden(self):
        for garden in self.ManagerGardens:
            print(f"{garden.garden_name}")

    @classmethod
    def create_garden_network(self, gardens):
        network = {}
        for garden in gardens:
            network[garden.garden_name] = []
        return network


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

    def show_plants(self):
        for plant in self.plants:
            print(f"{plant.name}")


alice = GardenManager("alice")
plant = Plant("Rose", 120, 50)

garden1 = Garden("garden")
garden1.add_plant(plant)
garden1.show_plants()

alice.add_garden(garden1)
alice.show_garden()

garden1 = Garden("Garden A")
garden2 = Garden("Garden B")
garden3 = Garden("Garden C")

network = GardenManager.create_garden_network(
    [garden1, garden2, garden3]
)

print(network)
