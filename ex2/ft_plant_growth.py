class Plant:
    """
    create the Plant class and set the name, age, height attributes
    """
    def __init__(self, name, height, Age):
        self.name = name
        self.Age = Age
        self.height = height
    """
    the grow method that increment the height by 1
    """
    def grow(self):
        self.height += 1
    """
    the age method that increment the age by 1
    """
    def age(self):
        self.Age += 1
    """
    the get_info method print informations about the plant
    """
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.Age} days old")


"""
creat the Rose object
"""
Rose = Plant("Rose", 25, 30)
first_height = Rose.height
"""
a for loop that call the methods get_inof , grow and age i days
"""
print("=== Day 1 ===")
Rose.get_info()
for i in range(1, 7):
    Rose.grow()
    Rose.age()
print("=== Day 7 ===")
Rose.get_info()
print(f"Growth this week: +{Rose.height - first_height}cm")
print()
"""
crear other plant named Sunflower
"""
Sunflower = Plant("Sunflower", 80, 40)
first_height = Sunflower.height
print("=== Day 1 ===")
Sunflower.get_info()
for i in range(1, 7):
    Sunflower.grow()
    Sunflower.age()
print("=== Day 7 ===")
Sunflower.get_info()
print(f"Growth this week: +{Sunflower.height - first_height}cm")
