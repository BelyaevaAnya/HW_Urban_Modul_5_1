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

    def __len__(self):
        return self.age
    
    def __del__(self):
        print(f'{self.name} ушел')

den = Human('Денчик', 23)
max = Human('Максон', 35)
den.surname = "Попов"
den.birthday()
max.birthday()
print(id(den), den.name, den.age, den.surname)

del den
print(len(max))
# den.say_info()
# max.say_info()
print(id(max), max.name, max.age)
