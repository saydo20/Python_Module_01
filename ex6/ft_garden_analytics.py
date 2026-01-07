class GardenManager:
    """create a class variable the will store how many garden been managed"""
    Total_gardens_managed = 0
    """the constructor to creat the attributes"""
    def __init__(self, name):
        self.name = name
        self.stats = self.GardenStats()
        self.ManagerGardens = []
    """create the inner class that will responsible for the statistics"""
    class GardenStats:
        def __init__(self):
            self.Gardens = []
        """the methode that add garden """
        def add_garden(self, garden):
            self.Gardens = self.Gardens + [garden]
        """calculate how many plants among all the gardens"""
        def calculate_plants_in_gardens(self):
            i = 0
            for garden in self.Gardens:
                for plant in garden.plants:
                    i += 1
            return i
        """print a report about the garden"""
        def garden_report(self, garden):
            print("=== Alice's Garden Report ===")
            print("Plants in garden:")
            for plant in garden.plants:
                if "_Prize_points" in plant.__dict__:
                    print(f"- {plant.name}: {plant.get_height()}cm,"
                          f" {plant.color} flowers {plant.bloom()},"
                          f" Prize point: {plant._Prize_points}")
                elif "color" in plant.__dict__:
                    print(f"- {plant.name}: {plant.get_height()}cm,"
                          f" {plant.color} flowers {plant.bloom()}")
                else:
                    print(f"- {plant.name}: {plant.get_height()}cm")
        """count how many plants for each type"""
        def count_types(self, garden):
            prize = 0
            flowering = 0
            regular = 0
            """
            use the __dict__ to search if the object contain the attribute
            """
            for plant in garden.plants:
                if "_Prize_points" in plant.__dict__:
                    prize += 1
                elif "color" in plant.__dict__:
                    flowering += 1
                else:
                    regular += 1
            print(f"Plant types: {regular} regular,"
                  f" {flowering} flowering, {prize} prize flowers")
        """
        count the score of each manager
        score = total height of all the plant + total prize point * 4
        """
        def count_score(self, garden):
            score_count = 0
            prize_total = 0
            for plant in garden.plants:
                score_count += plant.get_height()
            for plant in garden.plants:
                if "_Prize_points" in plant.__dict__:
                    prize_total += plant.get_prize_points()
            return score_count + prize_total * 4
    """
    the add garden methode for the garden manager object
    and call the methode that is in stats to
    """
    def add_garden(self, garden):
        self.ManagerGardens = self.ManagerGardens + [garden]
        self.stats.add_garden(garden)
        GardenManager.Total_gardens_managed += 1
    """add a plant to the garden"""
    def add_plant(self, garden, plant):
        garden.add_plant(plant)
        print(f"Added {plant.name} to {self.name}'s garden")
    """the helper methode that help the plant to grow"""
    def grow(self, garden):
        print(f"{self.name} is helping all plants grow...")
        couter = 0
        for plant in garden.plants:
            plant.grow()
            couter += 1
        return couter
    """ method that works on the manager type itself"""
    @classmethod
    def create_garden_network(cls, gardens):
        network = {}
        for garden in gardens:
            network[garden.garden_name] = []
        return network
    """static methode to chaeck if the height id valid or not"""
    @staticmethod
    def valid_height(height):
        return height > 25


class Plant:
    """create the palnt class (the parent class"""
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
    """setter for the age"""
    def set_age(self, age_value):
        if age_value < 0:
            print("Invalid operation attemped"
                  f"age {age_value}days [REJECTED]")
        else:
            self._age = age_value
            print(f"Age updated: {self._age}days [OK]")
    """setter for the height"""
    def set_height(self, height_value):
        if height_value < 0:
            print("Invalid operation attemped"
                  f"height {height_value}cm [REJECTED]")
        else:
            self._height = height_value
            print(f"Height updated: {self._height}")
    """grow methode that makes the plant object to grow"""
    def grow(self):
        self._height += 1
        print(f"{self.name} grow 1cm")
    """getter for the height"""
    def get_height(self):
        return self._height
    """getter for the age"""
    def get_age(self):
        return self._age


class FloweringPlant(Plant):
    """the flowering plant class that inhiret form the plant class"""
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    """blooming methode"""
    def bloom(self):
        return "(blooming)"


class PrizeFlower(FloweringPlant):
    """the prize flower class that inhiret from the plant class"""
    def __init__(self, name, height, age, color, Prize_points):
        super().__init__(name, height, age, color)
        self._Prize_points = Prize_points
    """setter for the points"""
    def set_points(self, points_value):
        if points_value < 0:
            print(f"the value{points_value} is [REJECTED] NON NIGATIVE VALUE")
        else:
            self._Prize_points = points_value
            print(f"the value {points_value} is updated [OK]")
    """getter for the prize points"""
    def get_prize_points(self):
        return self._Prize_points


class Garden:
    """the garden class"""
    def __init__(self, garden_name):
        self.garden_name = garden_name
        """creat a list that will store the objects of the plants"""
        self.plants = []
    """the add plant methode that add a plant to the list"""
    def add_plant(self, plant):
        self.plants = self.plants + [plant]


"""the main that we will test all the program"""
if __name__ == "__main__":
    plant1 = Plant("plant1", 40, 50)
    plant2 = Plant("plant2", 52, 50)
    garden2 = Garden("garden2")
    garden2.add_plant(plant1)
    garden2.add_plant(plant2)
    bob = GardenManager("Bob")
    bob.add_garden(garden2)
    """
    create the plant1 and the plant2
    create the garden2 and add the plants 1 and 2 to it
    creat the bob garden manager and add the garden2 to it
    this test is for matching the example in the subject
    """
    print("=== Garden Management System Demo ===")
    print()
    Oak = Plant("Oak Tree", 100, 1800)
    Rose = FloweringPlant("Rose", 25, 20, "red")
    Sunflower = PrizeFlower("Sunflower", 50, 25, "yellow", 10)
    Garden = Garden("Garden")
    alice = GardenManager("Alice")
    """
    create the plants : Oak tree, Rose, Sunflower.
    create the garden that will store this plants
    alice, the garden manager of this garden
    """
    initial_plants = alice.stats.calculate_plants_in_gardens()
    """store the unitial amount of plant to calcuate how many are added"""
    alice.add_garden(Garden)
    alice.add_plant(Garden, Oak)
    alice.add_plant(Garden, Rose)
    alice.add_plant(Garden, Sunflower)
    """alice start managing the garen and add the plant to the garden"""
    print()
    grow_counter = alice.grow(Garden)
    """
    call the grow methode to help the plant to grow
    store the return value of the methode that is the grow couter
    """
    print()
    alice.stats.garden_report(Garden)
    """print the report of the garden statistics"""
    print()
    final_plants = alice.stats.calculate_plants_in_gardens()
    print(f"Plants added: {final_plants - initial_plants},"
          f" Total growth: {grow_counter}cm")
    """print how many plant are added"""
    alice.stats.count_types(Garden)
    print()
    print("Height validation test:",
          GardenManager.valid_height(Oak.get_height()))
    """check if the height are valid or not"""
    print(f"Garden scores - {alice.name}: {alice.stats.count_score(Garden)}, "
          f"{bob.name}: {bob.stats.count_score(garden2)}")
    """print the score of the garden managers alice and Bob"""
    print(f"Total gardens managed: {GardenManager.Total_gardens_managed}")
    """print the total garden are been managed"""
