# Задайте число. 
# Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def gen_nega_fib_list(count):
    nega_list = [0, 1]
    
    for _ in range(2, count):                                      # немного изменил вывод, чтобы число, которое вводишь соответствовало количеству элементов последовательности, включая 0
        nega_list.append(nega_list[-2] - nega_list[-1])
    
    nega_list.reverse()
    
    for _ in range(1, count):
        nega_list.append(nega_list[-1] + nega_list[-2])
    
    return nega_list

    
k = 9

if k == 0:
    print([])
elif k == 1:
    print([0])
else:
    nega_fib_list = gen_nega_fib_list(count = k)
    print(nega_fib_list)