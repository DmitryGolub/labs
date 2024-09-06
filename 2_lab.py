# задание 1
def greet(name):
    s = f'Hello, {name}'
    print(s)


def square(number):
    return number ** 2


def max_to_two(number_first, number_second):
    return number_first if number_first > number_second else number_second

# задание 2
def describe_person(name, age=30):
    s = f'Your name: {name}. Your age: {age}'
    print(s)


def is_prime(number):
    a = []
    for i in range(1, number+1):
        if number % i == 0:
            a.append(i)

    return not len(a) > 2
