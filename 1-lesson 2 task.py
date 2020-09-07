user_sec = int((input("Введите время в секундах:")))
hours = user_sec // 3600
min = (user_sec % 3600) // 60
sec = (user_sec % 3600) % 60
print(f"Сейчас {hours:02d}:{min:02d}:{sec:02d}")