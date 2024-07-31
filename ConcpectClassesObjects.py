class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        print(f'Привет! Меня зовут {self.name}, мне {self.age}')


den = Human('Денчик', 23)
max = Human('Максон', 35)
den.surname = "Попов"
den.say_info()
max.say_info()
print(id(den), den.name, den.age, den.surname)
print(id(max), max.name, max.age)
