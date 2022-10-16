# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции. *Пример:*  45 -> 101101;  3 -> 11;  2 -> 10

def convert_number(number10):
    number2 = ''
 
    while number10 > 0:
        residual = str(number10 % 2)
        number2 = residual + number2
        number10 = number10 // 2
 
    return number2

try:
    x= int(input('Введите натуральное десятичное число: '))
    res= convert_number(x)
    print(res)
except ValueError as ex:
    print('Введите число!')
    exit(ex)