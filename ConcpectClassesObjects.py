class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # вызываем при инициализации объекта
        self.say_info()

    def say_info(self):
        print(f'Привет! Меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print(f'У меня день рождения!!! Мне теперь {self.age}')
    def __str__(self):
        return self.name
    def __len__(self):
        return self.age
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        return self.age == other.age or self.name == other.name
    def __bool__(self):
        return bool(self.age)
    def __del__(self):
        print(f'{self.name} ушел')

den = Human('Денчик', 23)
max = Human('Максон', 35)
den.surname = "Попов"
den.birthday()
max.birthday()
# print(id(den), den.name, den.age, den.surname)
# print(id(max), max.name, max.age)
# if den:
#     den.say_info()
# print(max)
# => Привет! Меня зовут Денчик, мне 24
# print(den < max)
# print(den > max)
# print(den == max)
# max.name = 'Денчик'
# print(den == max)
# => True
# self.age < other.age __lt__
# True
# False
# False
# a = 6
# print(den)
# del den
# print(len(max))
# den.say_info()
# max.say_info()
