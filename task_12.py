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
        if isinstance(self.calories, int | float) and self.calories < 200.0:
            return True
        else:
            return False

    def is_delicious(self):
        if isinstance(self, Dessert):
            return True
        else:
            return False


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None):
        super().__init__(name, calories)
        self.flavor = None

    def get_flavor(self):
        return self.flavor

    def set_flavor(self, flavor="standart"):
        self.flavor = flavor

    def is_delicious(self):
        if super().is_healthy() or self.flavor == "black licorice":
            return False
        else:
            return True
