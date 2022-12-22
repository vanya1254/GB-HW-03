# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def gen_list_num(count):
    new_list = []
    
    for _ in range(count):
        new_list.append(randint(-10, 10))
    
    return new_list


def sum_odd_index_num(new_list):
    odd_index_list = []
    sum = 0
    
    for i in range(1, len(new_list), 2):
        sum += new_list[i]
        odd_index_list.append(new_list[i])
        
    return odd_index_list, sum


count_num = 5
rnd_list = gen_list_num(count_num)
odd_list, sum_nums = sum_odd_index_num(rnd_list)

print(rnd_list)
print(f"На нечетных позициях элементы {odd_list}, ответ: {sum_nums}")
# print("На нечетных позициях элементы " + ('{} '*len(odd_list)).format(*odd_list) + f"ответ: {sum_nums}")