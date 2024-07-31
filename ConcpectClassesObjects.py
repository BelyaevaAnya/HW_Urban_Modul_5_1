class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


den = Human('Денчик', 23)
max = Human('Максон', 35)
print(id(den), den.name, den.age)
print(id(max), max.name, max.age)