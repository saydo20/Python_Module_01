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

        def calculate_gardens(self):
            i = 0
            for garden in self.Gardens:
                i += 1
            print(f"the total gardens is {i}")

        def calculate_plants_in_gardens(self):
            i = 0
            for garden in self.Gardens:
                for plant in garden.plants:
                    i += 1
            return i

        def garden_report(self, garden):
            print("=== Alice's Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                if "_Prize_points" in plant.__dict__:
                    print(f"- {plant.name}: {plant.get_height()},"
                          f" {plant.color} flowers {plant.bloom()},"
                          f" Prize point: {plant._Prize_points}")
                elif "color" in plant.__dict__:
                    print(f"- {plant.name}: {plant.get_height()},"
                          f" {plant.color} flowers {plant.bloom()},")
                else:
                    print(f"- {plant.name}: {plant.get_height()}")

        def count_types(self, garden):
            prize = 0
            flowering = 0
            regular = 0
            for plant in garden.plants:
                if "_Prize_points" in plant.__dict__:
                    prize += 1
                elif "color" in plant.__dict__:
                    flowering += 1
                else:
                    regular += 1
            print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

    def add_garden(self, garden):
        self.ManagerGardens = self.ManagerGardens + [garden]
        self.stats.add_garden(garden)

    def show_garden(self):
        for garden in self.ManagerGardens:
            print(f"{garden.garden_name}")

    def add_plant(self, garden, plant):
        garden.add_plant(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow(self, garden):
        print(f"{self.name} is helping all plants grow...")
        couter = 0
        for plant in garden.plants:
            plant.grow()
            couter += 1
        return couter

    @classmethod
    def create_garden_network(cls, gardens):
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

    def grow(self):
        self._height += 1
        print(f"{self.name} grow 1cm")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return "(blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, Prize_points):
        super().__init__(name, height, age, color)
        self._Prize_points = Prize_points

    def set_points(self, points_value):
        if points_value < 0:
            print(f"the value{points_value} is [REJECTED] NON NIGATIVE VALUE")
        else:
            self._Prize_points = points_value
            print(f"the value {points_value} is updated [OK]")


class Garden:
    def __init__(self, garden_name):
        self.garden_name = garden_name
        self.plants = []

    def add_plant(self, plant):
        self.plants = self.plants + [plant]

    def show_plants(self):
        for plant in self.plants:
            print(f"{plant.name}")


print("=== Garden Management System Demo ===")
print()
Oak = Plant("Oak Tree", 100, 1800)
Rose = FloweringPlant("Rose", 25, 20, "red")
Sunflower = PrizeFlower("Sunflower", 50, 25, "yellow", 10)
Garden = Garden("Garden")
alice = GardenManager("Alice")
initial_plants = alice.stats.calculate_plants_in_gardens()
alice.add_garden(Garden)
alice.add_plant(Garden, Oak)
alice.add_plant(Garden, Rose)
alice.add_plant(Garden, Sunflower)
print()
grow_counter = alice.grow(Garden)
print()
alice.stats.garden_report(Garden)
print()
final_plants = alice.stats.calculate_plants_in_gardens()
print(f"Plants added: {final_plants - initial_plants},"
      f" Total growth: {grow_counter}cm")
alice.stats.count_types(Garden)










# garden1 = Garden("Garden A")
# garden2 = Garden("Garden B")
# garden3 = Garden("Garden C")

# network = GardenManager.create_garden_network([garden1, garden2, garden3])

# print(network)


