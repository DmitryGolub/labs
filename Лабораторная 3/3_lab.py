# задание 1

with open('files/example.txt', 'r', encoding='utf-8') as file:
    # первый способ чтения
    text = file.read()
    print(text)

with open('files/example.txt', 'r', encoding='utf-8') as file:
    # второй способ чтения
    for line in file:
        print(line, end='')


# задание 2
print('Введите /end, если хотите закончить ввод текста')
with open('files/user_input.txt', 'a', encoding='utf-8') as file:
    text = input('>>> ')
    while text != '/end':
        file.write(text + '\n')
        text = input('>>> ')


# задание 3
try:
    print('Введите /end, если хотите закончить ввод текста')
    with open('files/user_input.txt', 'a', encoding='utf-8') as file:
        text = input('>>> ')
        while text.lower().strip() != '/end':
            file.write(text + '\n')
            text = input('>>> ')

except FileNotFoundError:
    print('Файл не найден')

