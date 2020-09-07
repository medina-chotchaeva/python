gain = int(input("Введите выручку: "))
expenses = int(input("Введите издержки: "))
if gain > expenses:
    profit = gain - expenses
    print(f"Ваша прибыль составляет {profit}")
    rent = profit / gain
    print(f"Рентабельность {rent}")
    employee = int(input("Сколько у вас сотрудников: "))
    print(f"Прибыль фирмы в расчёта на одного сотрудника равна {profit / employee}")
elif gain == expenses:
    print("Ваша прибыль равна нулю")
else:
    print("Ваша фирма работает в убыток")