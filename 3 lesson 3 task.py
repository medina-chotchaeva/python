def my_func (val_1, val_2, val_3):
    row = [val_1, val_2, val_3]
    min_val = min(row)
    row.remove(min_val)
    print(sum(row))
my_func(1, 7, 564)