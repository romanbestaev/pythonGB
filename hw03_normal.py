# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    # Начальные данные
    left,right,i = 1,1,3
    fib_list = []
    while i <= m:
        i += 1
        fib = left + right
        left,right = right,fib
        if i >= n:
            fib_list.append(fib)
    return fib_list

print(fibonacci(5,10))
print(fibonacci(6,11))
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    if origin_list:
        return (
               sort_to_max([x for x in origin_list if x < origin_list[0]]) + 
                           [x for x in origin_list if x == origin_list[0]] + 
               sort_to_max([x for x in origin_list if x > origin_list[0]])
               )
    return []

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(fun,a):
    return [x for x in a if fun(x)]

number_list = range(-5, 5)
print('\n')
print(my_filter(lambda x: x < 0, number_list))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def is_paralel(A1, A2, A3, A4):
    '''Если в четырехугольнике противоположные стороны попарно равны, 
       то этот четырехугольник — параллелограмм'''
    import numpy as np
    a1 = np.array(A1)
    a2 = np.array(A2)
    a3 = np.array(A3)
    a4 = np.array(A4)
    if np.linalg.norm(a2-a1) == np.linalg.norm(a4-a3):
        res = 'Да'
    elif np.linalg.norm(a3-a1) == np.linalg.norm(a4-a2):
        res = 'Да'
    else:
        res = 'Нет'    
    return res

print('\n')
print(is_paralel( (0,0),(10,0),(1,1),(11,1) ))
print(is_paralel( (0,0),(10,0),(1,1),(12,1) ))