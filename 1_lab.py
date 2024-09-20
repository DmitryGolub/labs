def validator_1(data):
    try:
        n = int(data)

        if n < 1:
            print(" -- Число должно быть больше 0 -- ")
            return False
    except Exception as ex:
        print(" -- Ошибка при вводе данных, повторите попытку -- ")
        return False
    return n


# первая задача
number = input('Введите число: ')

while not validator_1(number):
    number = input('Введите число: ')

number = validator_1(number)

for num in range(1, number + 1):
    print(num)


def validator_2(data):
    try:
        n = float(data)
    except Exception as ex:
        print(" -- Ошибка при вводе данных, повторите попытку -- ")
        return False
    return n


# вторая задача
first_number = input('Введите первое число: ')

while not validator_2(first_number):
    first_number = input('Введите первое число: ')

second_number = input('Введите второе число: ')

while not validator_2(second_number):
    second_number = input('Введите второе число: ')

print(first_number if first_number > second_number else second_number)
