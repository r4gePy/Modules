def password_level(password):
    if password == '-':
        quit()
    if len(password) < 6:
        return "Недопустимый пароль"
    elif password.isdigit is True or password.isupper() or password.islower():
        return "Ненадёжный пароль"
    elif password.isalpha() \
            or password.isalpha() and password.islower() \
            or password.isalpha() and password.isupper() \
            or password.isalnum() and password.islower()\
            or password.isalnum() and password.isupper():
        return "Слабый пароль"
    else:
        return "Надёжный пароль"


print(password_level(input('Введите проверяемый пароль ')))

answer = input('Хотите проверить надёжность ещё одного пароля, Ответьте "+" или "-" ')
while True:
    if answer == '+':
        print(password_level(input('Введите пароль на проверку ')))
    elif answer == '-':
        quit()
    else:
        answer = input('Вы ввели неизвестный знак, пожалуйста введите необохдимый символ("+" "-") ')
