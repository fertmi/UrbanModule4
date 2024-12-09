from math import inf #В библиотеке math вызываем только inf (бесконечность)

#Функция деления чисел, при делении на ноль выдает результат бесконечность
def divide(first, second):
    if second == 0:
        return inf
    return first/second