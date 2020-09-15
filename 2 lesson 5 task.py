number = int(input("Введите число: "))
list = [9, 7, 5, 3, 1]
a = list.count(number)
for element in list:
    if a > 0:
        num_index = list.index(number)
        list.insert(num_index + a, number)
        break
    else:
        if number > element:
            el_index = list.index(element)
            list.insert(el_index, number)
            break
        elif number < list[len(list) - 1]:
            list.append(number)
print(list)