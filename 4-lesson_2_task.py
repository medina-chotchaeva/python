my_list = [143, 345, 25, 124, 63]
print(my_list)
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new_list)