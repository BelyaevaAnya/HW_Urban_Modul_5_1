class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

    # если пароль содержит 1 символ в верхнем регитре
    # и если пароль содержит цифры


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Привет! Выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            if login in database.data:
                print('Логин есть в системе')
            else:
                print('Логина нет в системе')
                break
            password = input('Введите пароль: ')
            if password == database.data[login]:
                print(f'Вы вошли в систему, {login} :)')
                continue
            else:
                print('Пароль не совбадает с паролем в базе данных. Вы не можете войти!')
                break
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password_copy := input('Повториите пароль: '))
            if password != password_copy:
                print('Ошибка! Пароли не совпадают :( Попробуйте еще раз.')
                continue
            database.add_user(user.username, user.password)
            print(database.data)
        else:
            exit()
