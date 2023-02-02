from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side) -> None:
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


class Rect(Shape):
    def __init__(self, length, width) -> None:
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2


square = Square(10)
print(f"square area is {square.area()} and perimeter is {square.perimeter}")
rect = Rect(5, 3)
print(f"rectangle area is {rect.area()} and perimeter is {rect.perimeter}")
