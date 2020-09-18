#первый вариант
def my_func(x,y):
    result = x ** y
    return result
print(my_func(float(input("Введите действительное положительное число ")), int(input("Введите целое отрицательное число "))))

#второй вариант
def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result
print(my_func(float(input("Введите действительное положительное число ")), int(input("Введите целое отрицательное число "))))