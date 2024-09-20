# задание 1

with open('files/example.txt', 'r', encoding='utf-8') as file:
    # первый способ чтения
    text = file.read()
    print(text)

with open('files/example.txt', 'r', encoding='utf-8') as file:
    # второй способ чтения
    for line in file:
        print(line)


# задание 2
with open('files/user_input.txt', 'a', encoding='utf-8') as file:
    text = input('>>> ')
    while text != '/end':
        file.write(text + '\n')
        text = input('>>> ')


# задание 3
try:
    with open('file/user_input.txt', 'a', encoding='utf-8') as file:
        text = input('>>> ')
        while text != '/end':
            file.write(text + '\n')
            text = input('>>> ')
except FileNotFoundError:
    print('Файл не найден')

