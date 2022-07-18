# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import math
from unittest import result

def sum_of_number_odd_position(lst_of_number: list):
    sum_of_number=0
    user_massage = "Not a digit elements with index: "
    for i in range(1,len(lst_of_number),2):
        try:
            sum_of_number+=lst_of_number[i]
        except:
            user_massage+=f"{i} | "
    return [sum_of_number, user_massage]

# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def product_of_a_pair(lst_numbers: list):
    result = []
    error_massage = None
    size_lst = math.ceil(len(lst_numbers)/2)
    for i in range(0,size_lst):
        try:
            temp = int(lst_numbers[i])*int(lst_numbers[0-1-i])
            result.append(temp)
        except:
            error_massage = "There is an element in user list that is not a digit"
    return [result, error_massage]

# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564

def difference_min_vs_max_fp(lst_number: list):
    min = round(lst_number[0]-int(lst_number[0]),3)
    max = round(lst_number[0]-int(lst_number[0]),3)
    error_massage = None
    result = 0
    try:
        for i in range(0,len(lst_number)):
            temp = round(lst_number[i]-int(lst_number[i]),3)
            if float(temp) < min:
                min = temp
            elif float(temp) > max:
                max = temp
        result = round(max - min,3)
    except:
        error_massage = "There is an element in user list that is not a digit"
    return [result, error_massage]


# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_in_binary (user_number: int):
    result = ""
    if user_number > 1:
        if user_number % 2 == 0:
            result = '0' 
        else:
            result = '1'
        user_number = user_number // 2
        return  decimal_in_binary (user_number) + result
    else:
        return str(user_number) + result

# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# -2 = -1| -1 = 1 |1 = 1| 2 = 1


def negafibonacci (user_number: int):
        if user_number == -2:
            return (-1)
        elif user_number in [-1, 1, 2]:
            return (1)
        elif user_number == 0:
            return (0)
        elif user_number < 2:
            return (negafibonacci(user_number + 2) - negafibonacci(user_number +1))
        else:
            return (negafibonacci(user_number - 1) + negafibonacci(user_number - 2))     
def sequence_negafibonacci(user_number:int):
    if type(user_number) == int:
        result = []
        for i in range (-abs(user_number), user_number+1):
            result.append(negafibonacci(i))
        return result
    else:
        return 'You enter not a digit'


