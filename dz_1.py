"""
Задание № 1

Реализовать функцию, принимающую два числа (позиционные аргументы)и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""

def division():

    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if b == 0:
        print('На ноль делить нельзя, попробуй ещё раз.')
        return
    result = a / b

    print(f'Результат выражения {a}/{b} = {result:.2f}')

division()
