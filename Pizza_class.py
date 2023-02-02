# exampel of making many constructors in a class
class Pizza:
    def __init__(self, radius, ingredients) -> None:
        self.radius = radius
        self.__ingredients = ingredients

    @staticmethod
    def circle_area(r):
        return r ** 2 * Math.PI()

    def area(self):
        return Pizza.circle_area(self.radius)

    @classmethod
    def veg(cls):
        return cls(["mushrooms", "olives", "onions"])

    @classmethod
    def margherita(cls):
        return cls(["mozarella", "sauce"])

    def __str__(self) -> str:
        return f"Pizza ingredients are {self.__ingredients}"


class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def add5(num):
        return num + 5

    @staticmethod
    def add10(num):
        return num + 10

    @staticmethod
    def PI():
        return 3.14


x = Math.add(5, 10)
y = Math.add5(x)
z = Math.add10(y)
