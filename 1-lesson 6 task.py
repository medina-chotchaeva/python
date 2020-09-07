a = int(input("Результат первого дня: "))
b = int(input("Желаемый результат: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a * 10 / 100
    day += 1
print(day)