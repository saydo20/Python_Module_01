class Plant:

    """create the Plant class and set the name, age, height attributes"""
    def __init__(self, name, height_plant, age_plant):
        self.name = name
        self.age_plant = age_plant
        self.height_plant = height_plant

    """the grow method that increment the height by 1"""
    def grow(self):
        self.height_plant += 1

    """the age method that increment the age by 1"""
    def age(self):
        self.age_plant += 1

    """the get_info method print informations about the plant"""
    def get_info(self):
        print(f"{self.name}: {self.height_plant}cm, {self.age_plant} days old")


if __name__ == "__main__":

    """creat the rose object"""
    rose = Plant("Rose", 25, 30)
    first_height = rose.height_plant

    """a for loop that call the methods get_inof , grow and age i days"""
    print("=== Day 1 ===")
    rose.get_info()
    i = 1
    while i < 7:
        rose.grow()
        rose.age()
        i += 1
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height_plant - first_height}cm")
    print()

    """crear other plant named sunflower"""
    sunflower = Plant("Sunflower", 80, 40)
    first_height = sunflower.height_plant
    print("=== Day 1 ===")
    sunflower.get_info()
    i = 1
    while i < 7:
        sunflower.grow()
        sunflower.age()
        i += 1
    print("=== Day 7 ===")
    sunflower.get_info()
    print(f"Growth this week: +{sunflower.height_plant - first_height}cm")
