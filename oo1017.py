class Person:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def getbmi(self):
        return self.weight / (self.height / 100) ** 2

    def __str__(self):
        return "{}\t{}\t{}".format(self.name,
                                   self.height,
                                   self.weight)

    def __repr__(self):
        return self.__str__()


class SuperPerson(Person):

    def __init__(self, name, height, weight, age):
        Person.__init__(self, name, height, weight)
        self.age = age

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(self.name,
                                       self.height,
                                       self.weight,
                                       self.age)
    def __repr__(self):
        return self.__str__()

p1 = Person("Elwing", 175, 75)
print(p1)
print(p1.getbmi())
# print(Person.getbmi(p1))
p2 = SuperPerson("Bob", 180, 80, 18)
print(p2)
print([p1, p2])