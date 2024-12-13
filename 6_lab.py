import re


class UserAccount():
    def __init__(self, username, email, password):
        self.username = self.validator_username(username)
        self.email = self.validator_email(email)
        self.__password = self.validator_password(password)

    def set_password(self, new_password):
        self.__password = self.validator_password(new_password)

    def check_password(self, password):
        return self.__password == password

    @classmethod
    def validator_username(cls, data):
        if not isinstance(data, str):
            raise ValueError("Тип данных должен быть str")
        if len(data) < 2:
            raise ValueError("Имя должно состоять минимум из 2 символов")
        return data

    @classmethod
    def validator_email(cls, data):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not isinstance(data, str):
            raise ValueError("Тип данных должен быть str")
        if not re.match(email_pattern, data):
            raise ValueError("Некорректная почта")
        return data

    @classmethod
    def validator_password(cls, data):
        if not isinstance(data, str):
            raise ValueError("Тип данных должен быть str")
        if len(data) < 6:
            raise ValueError("Пароль должен состоять минимум из 6 символов")
        return data


class Vehicle:
    def __init__(self, mark, model):
        self.__mark = mark
        self.__model = model

    def get_info(self):
        return f"Марка - {self.__mark} Модель - {self.__model}"
#       raise ValueError('Переопределите метод')


class Car(Vehicle):
    def __init__(self, mark, model, fuel_type):
        super().__init__(mark, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return super().get_info() + f" Топливо - {self.fuel_type}"


account_1 = UserAccount("Anton", "anton123@gma.lcom", "2323asfdsdf")
account_1.set_password("23234sadfsfas")
print(account_1.check_password("23234"))
print(account_1.check_password("23234sadfsfas"))
print(account_1.check_password(1232412))

car = Car("BMW", "m5 f90", "petrol 95")
print(car.get_info())
# спросить подробнее про полиморфизм, про переопределение методов
