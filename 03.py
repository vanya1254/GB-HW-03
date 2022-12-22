# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, 
# отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint, uniform

def gen_list_float_num(count):
    new_list = []
    
    for _ in range(count):
        index = randint(0, 2)
        new_list.append(round(uniform(0, 10), index))
    
    return new_list


def gen_list_remainder(new_list):
    remainder_list = []
    
    for i in new_list:
        remainder_num = round(i % 1 * 100, 0)
        remainder_list.append(remainder_num)
    # print(remainder_list)
    return remainder_list

def diff_min_max_remainder(remainder_list):
    while True:
        if min(remainder_list) == 0:
            remainder_list.remove(0)
        else:
            break
    
    diff = (max(remainder_list) - min(remainder_list)) / 100
    # print(max(remainder_list), min(remainder_list))
    return round(diff, 2)


count_num = 5
rnd_list = gen_list_float_num(count_num)
print(rnd_list)

rnd_remainder_list = gen_list_remainder(rnd_list)
diff_min_max = diff_min_max_remainder(rnd_remainder_list)
print(diff_min_max)