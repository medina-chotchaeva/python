from sys import argv

name, prod_in_hour, hour_rate, premium = argv

prod_in_hour = int(prod_in_hour)
hour_rate = int(hour_rate)
premium = int(premium)

print("Заработная плата: ", prod_in_hour * hour_rate + premium)