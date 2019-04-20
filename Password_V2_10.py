def password_2in1():
    import random

    # Блок генерации пароля

    list_symbols_numbers = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
                            'Q', "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M",
                            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+'
                            ]
    list_words = []
    password = []
    max_length = int(input('Введите максимальную длину пароля '))

    # Заполнение нового списка рандомными символами
    for x in range(max_length):
        random_symbol = random.randint(0, len(list_symbols_numbers) - 1)
        password.append(list_symbols_numbers[random_symbol])

    # склейка нового списка в переменную
    ready_pass = ''.join(password)

    # Конец блока генерации пароля

    print(ready_pass)

    # Блок проверки на надёжность
    answer = input('Желаете проверить надёжность сгенерированного пароль? '
                   '(Ответьте "+" или "-") ')
    if answer == '+':
        if len(ready_pass) < 6:
            return "Недопустимый пароль"
        elif ready_pass.isdigit is True or ready_pass.isupper() or ready_pass.islower():
            return "Ненадёжный пароль"
        # Проверка по регистру и наличию цифр или букв
        elif ready_pass.isalpha() \
                or ready_pass.isalpha() and ready_pass.islower() \
                or ready_pass.isalpha() and ready_pass.isupper() \
                or ready_pass.isalnum() and ready_pass.islower() \
                or ready_pass.isalnum() and ready_pass.isupper():

            return "Слабый пароль"
        else:
            return "Надёжный пароль"
    else:
        quit()
    # Конец блока проверки


# Вывод
global_pass = password_2in1()
print(global_pass)
