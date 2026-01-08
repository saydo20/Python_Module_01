class Plant:

    """create the Plant class and set the name, age, height attributes"""
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    """the grow method that increment the height by 1"""
    def grow(self):
        self.height += 1

    """the age method that increment the age by 1"""
    def age(self):
        self.age += 1

    """the get_info method print informations about the plant"""
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":

    """creat the rose object"""
    rose = Plant("Rose", 25, 30)
    first_height = rose.height

    """a for loop that call the methods get_inof , grow and age i days"""
    print("=== Day 1 ===")
    rose.get_info()
    for i in range(1, 7):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week: +{rose.height - first_height}cm")
    print()

    """crear other plant named sunflower"""
    sunflower = Plant("Sunflower", 80, 40)
    first_height = sunflower.height
    print("=== Day 1 ===")
    sunflower.get_info()
    for i in range(1, 7):
        sunflower.grow()
        sunflower.age()
    print("=== Day 7 ===")
    sunflower.get_info()
    print(f"Growth this week: +{sunflower.height - first_height}cm")
