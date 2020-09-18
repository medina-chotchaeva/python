def inf(name, surname, birth_date, city, email, tel):
    name = input("Имя: ")
    surname = input("Фамилия: ")
    birth_date = input("Год рождения: ")
    city = input("Город проживания: ")
    email = input("Адрес электронной почты: ")
    tel = input("Телефон: ")
    return ', '.join([name, surname, birth_date, city, email, tel])
print (inf(name = '',  surname = '',   birth_date = '', city = '',  email = '',  tel = ''))