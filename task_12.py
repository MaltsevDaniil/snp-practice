class Dessert:
    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_calories(self):
        return self.calories

    def set_calories(self, calories):
        self.calories = calories

    def is_healthy(self):
        if self.calories is not None and self.calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        if self.is_healthy():
            return True
        else:
            return False


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None):
        super().__init__(name, calories)

    def get_flavor(self):
        return self.flavor

    def set_flavor(self, flavor="standart"):
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        else:
            return True