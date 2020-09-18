def calc():
    try:
        val_1 = float(input("Укажите делимое: "))
        val_2 = float(input("Укажите делитель: "))
        quot = val_1 / val_2
    except ValueError:
        return
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return quot
print (calc())