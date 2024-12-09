#Функция деления чисел, при делении на ноль выдает результат "Ошибка"
def divide(first, second):
    if second == 0:
        return 'Ошибка'
    return first/second