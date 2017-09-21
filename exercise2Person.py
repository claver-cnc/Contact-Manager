class Person:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Eit(Person):
    def __init__(self, eitName, eitNationality, funFact):
        super().__init__(eitName, eitNationality)
        self.funFact = funFact

    def ability(self):
        print("The EITs have ability to {}".format(self.funFact))


class Fellow(Person):
    def __init__(self, felName, felNationality, happiness_level):
        super().__init__(felName, felNationality)
        self.happiness_level = happiness_level

    def felEat(self):
        self.happiness_level += 1
        print("The Fellows happiness level is {} ".format(self.happiness_level))

    def felTeach(self):
        self.happiness_level -= 1
        print("The Fellows happiness level is {} ".format(self.happiness_level))


