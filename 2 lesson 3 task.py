seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца: "))
if month ==1 or month == 2 or month == 12:
        print(month, "месяц - это ", seasons_dict.get(1))
        print(month, "месяц - это ", seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(month, "месяц - это ", seasons_dict.get(2))
    print(month, "месяц - это ", seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(month, "месяц - это ", seasons_dict.get(3))
    print(month, "месяц - это ", seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(month, "месяц - это ", seasons_dict.get(4))
    print(month, "месяц - это ", seasons_list[3])
else:
        print("Такого месяца нет")