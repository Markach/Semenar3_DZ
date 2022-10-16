# Задача 1 Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import random

def create_list(num):
    list=[]
    for i in range(num):
        b= int(random()*10)
        list.append(b)
    return list   


try:
    n= int(input('Введите число, длинну списка: '))
    res= create_list(n)
    print(res)
except ValueError as ex:
    print('Введите число!')
    exit(ex)


def find_sum_uneven_position(arr):
    sum=0
    for i in range(len(arr)):
        if i % 2 !=0:
            sum +=arr[i]
    return sum        


print(f'Сумма элементов в списке стоящих на нечетных позициях = {find_sum_uneven_position(res)}')    
