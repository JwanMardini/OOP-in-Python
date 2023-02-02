from datetime import date


class Student:
    def __init__(self, name, age=0):
        self.__name = name
        self.__age = age

    # Another way to make more than 1 constructor
    @classmethod
    def initFromBirhYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def describe(self):
        print(f"my name is {self.__name} and my age is {self.__age}")

    def is_old(self, num):
        if self.__age <= num:
            print("student is not old")
        else:
            print("student is old")
