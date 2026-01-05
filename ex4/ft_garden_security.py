class SecurePlant:
    """create the object and print the message that the object is crearted"""
    def __init__(self, name, height, age):
        self.name = name
        """the age and the height are now protecteds"""
        self._age = age
        self._height = height
        print(f"Plant created: {self.name}")
    """the setter of the hieght and reject the nigative values"""
    def set_hieght(self, age_value):
        if age_value < 0:
            print()
            print("Invalid operation attempted :"
                  f"height {age_value}cm [REJECTED]")
            print("Security: Negative height rejected")
            print()
        else:
            self._age = age_value
            print(f"hieght updated: {self._height}cm [OK]")
    """the setter of the age and reject the nigative values"""
    def set_age(self, height_value):
        if height_value < 0:
            print()
            print("Invalid operation attempted :"
                  f"age {height_value}days [REJECTED]")
            print("Security: Negative age rejected")
            print()
        else:
            self._height = height_value
            print(f"age updated: {self._height}days [OK]")
    """create a getter of the height and the getter of the age"""
    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


"""print the readable output"""
print("=== Garden Security System ===")
Rose = SecurePlant("Rose", 20, 29)
Rose.set_age(25)
Rose.set_age(30)
Rose.set_hieght(-5)
print(
      f"Current plant : {Rose.name} "
      f"({Rose.get_height()}cm {Rose.get_age()} days)"
)
