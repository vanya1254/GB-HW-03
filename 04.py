# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# binary_num = []

# def convert_to_binary(decimal_num):
#     if decimal_num == 0:
#         return
#     else:
#         binary_num.append(decimal_num % 2)                    # рекурсия
#         decimal_num //= 2
#         convert_to_binary(decimal_num)


# dec_num = 45

# if dec_num == 0:
#     print(0)
# else:
#     convert_to_binary(dec_num)
#     binary_num.reverse()
#     print(*binary_num, sep='')



def convert_to_binary(decimal_num, binary_num = ''):
    while decimal_num != 0:
        binary_num += str(decimal_num % 2)
        decimal_num //= 2

    return binary_num

dec_num = 45

if dec_num == 0:
    print(0)
else:
    bin_num = convert_to_binary(dec_num)
    print(bin_num[-1::-1])