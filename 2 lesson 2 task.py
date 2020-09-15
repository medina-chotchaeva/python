quantity = int(input("Количество элементов: "))
list = []
i = 0
el = 0
while i < quantity:
    list.append(input("Значение списка: "))
    i += 1

for element in range(int(len(list)/2)):
        list[el], list[el + 1] = list [el + 1], list[el]
        el += 2
print(list)