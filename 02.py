# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

def gen_list_num(count):
    new_list = []
    
    for _ in range(count):
        new_list.append(randint(-10, 10))
    
    return new_list


# def multiple_start_end(new_list):
#     mult_list = []
    
#     if len(new_list) % 2 != 0:
#         for i in range(len(new_list) // 2):
#             mult_list.append(new_list[i] * new_list.pop())                   # тоже работает, почему-то решил, что нечитаемо, в итоге переписал и несильно читаемее стало 
#         mult_list.append(new_list[len(new_list) // 2 + 1]**2)                # единственное, что во втором варианте изначальный список не изменяется
#     else:
#         for i in range(len(new_list) // 2):
#             mult_list.append(new_list[i] * new_list.pop())
    
#     return mult_list


def multiple_start_end(new_list):
    mult_list = []

    if len(new_list) % 2 != 0:
        mid_num = new_list.pop(len(new_list) // 2)
        
        for i in range(len(new_list) // 2):
            mult_list.append(new_list[i] * new_list[-i - 1])
        mult_list.append(mid_num**2)
    else:
        for i in range(len(new_list) // 2):
            mult_list.append(new_list[i] * new_list[-i - 1])
    
    return mult_list
    
            
count_num = 5
rnd_list = gen_list_num(count_num)
print(rnd_list)

mult_start_end_list = multiple_start_end(rnd_list)
print(mult_start_end_list)