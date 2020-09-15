the_str = input("Введите строку из нескольких слов: ")
word = []
num = 1
for el in range(the_str.count(' ') + 1):
    word = the_str.split()
    if len(str(word)) <= 10:
        print(f" {num} {word [el]}")
        num += 1
    else:
        print(f" {num} {word [el] [0:10]}")
        num += 1