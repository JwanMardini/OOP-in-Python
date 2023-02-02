from datetime import date


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def display(self):
        return f"name is {self.name} and age is {self.age}"

    @classmethod
    def initFromBirthYear(cls, name, birthYear, extra):
        return cls(name, date.today().year - birthYear, extra)

# Inhertince


class Man(Person):
    gender = "Male"
    no_of_men = 0

    def __init__(self, name, age, voice) -> None:
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_men += 1

    def display(self):
        string = super().display()
        return string+f" and voice is {self.voice} and gender is {self.gender}"


class Woman(Person):
    gender = "Female"
    no_of_women = 0

    def __init__(self, name, age, hair) -> None:
        super().__init__(name, age)
        self.hair = hair
        Woman.no_of_women += 1

    def display(self):
        string = super().display()
        return string + f" and hair is {self.hair} and gender is {self.gender}"


woman = Woman("Soso", 30, "Curly")
man = Man("Jwan", 20, "hard")

man_1 = Man.initFromBirthYear("Jwan", 1990, "hard")
print(man_1.display())


woman_1 = Woman.initFromBirthYear("Soso", 1995, "Curly")
print(woman_1.display())

print(isinstance(woman, Man))
