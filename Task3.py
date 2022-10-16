# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов. *Пример:*  [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import random

def create_list(num):
    list=[]
    for i in range(num):
        b= round(float(random()*10,),2)  # округлила до 2х знаков
        list.append(b)
    return list   

try:
    n= int(input('Введите число, длинну списка: '))
    res= create_list(n)
    print(res)
except ValueError as ex:
    print('Введите число!')
    exit(ex)


def find_difference(res):
    res2=[]
    for i in range(len(res)):
        a=int((res[i]*100)%100)   #  изначально округляла до 2х знаков после запятой вводимое число в список, поэтому т.о отделяла дробную часть
        res2.append(a)
    max_num=res2[0]
    min_num=res2[0]
    for i in range(len(res2)):
        if res2[i]>max_num:
            max_num=res2[i]
        elif res2[i]<min_num:
            min_num=res2[i]  
    dif= max_num-min_num 
    dif2=float(dif/100)        
    return dif2


print(f'Разницу между максимальным и минимальным значением дробной части элементов = {find_difference(res)}')  