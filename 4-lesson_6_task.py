from itertools import count

start_number = int(input("Стартовое число: "))
stop_number = int(input("Конечное число "))
for el in count(start_number):
    if el > stop_number:
        break
    else:
        print(el)

from itertools import cycle
elements = input("Элементы списка: ")
out = int(input("Повторять до: "))
с = 0
for el in cycle(elements):
    if с > out:
        break
    print(el)
    с += 1