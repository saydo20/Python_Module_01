class Plant:
    Total_plants = 0
    """
    create the Plant class and set the name, age, height attributes
    """
    def __init__(self, name, height, Age):
        self.name = name
        self.Age = Age
        self.height = height
        Plant.Total_plants += 1
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
        print(f"{self.name} ({self.height}cm, {self.Age} days)")


"""
creat the list that will hold all the objects
"""
list = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cacus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]
"""
a loop for print all the objects
"""
print("=== Plant Factory Output ===")
for i in list:
    print("Created: ", end="")
    i.get_info()
print()
"""
get the value of the class variable
"""
print(f"Total plants created: {Plant.Total_plants}")
