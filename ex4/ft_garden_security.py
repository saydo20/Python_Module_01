class SecurePlant:

    """create the object and print the message that the object is crearted"""
    def __init__(self, name):
        self.name = name

        """the age and the height are now protecteds"""
        self._age = 0
        self._height = 0
        print(f"Plant created: {self.name}")

    """the setter of the age and reject the nigative values"""
    def set_age(self, age_value):
        if age_value < 0:
            print()
            print("Invalid operation attempted :"
                  f"days {age_value}days [REJECTED]")
            print("Security: Negative days rejected")
            print()
        else:
            self._age = age_value
            print(f"age updated: {self._age} days [OK]")

    """the setter of the age and reject the nigative values"""
    def set_height(self, height_value):
        if height_value < 0:
            print()
            print("Invalid operation attempted :"
                  f"height {height_value}cm [REJECTED]")
            print("Security: Negative height rejected")
            print()
        else:
            self._height = height_value
            print(f"height updated: {self._height}cm [OK]")

    """create a getter of the height and the getter of the age"""
    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


if __name__ == "__main__":

    """print the readable output"""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(
        f"Current plant: {rose.name} "
        f"({rose.get_height()}cm, {rose.get_age()} days)"
    )
