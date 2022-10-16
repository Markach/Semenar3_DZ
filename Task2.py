# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д. *Пример:* - [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]

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


def find_product_numbers(arr):
    arr2=[]
    n=int(len(arr)/2)
    for i in range(n):
        prod = arr[i]*arr[-(i+1)]
        arr2.append(prod)
        if len(arr)%2 !=0:
            num=len(arr)//2
            prod=arr[num]**2          
    arr2.append(prod)
    if len(arr)%2 ==0:
        arr2.pop(-1)
    return arr2        


print(f'Произведение пар чисел списка = {find_product_numbers(res)}')  