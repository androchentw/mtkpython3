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

p1 = Person("Elwing", 175, 75)
print(p1)
print(p1.getbmi())