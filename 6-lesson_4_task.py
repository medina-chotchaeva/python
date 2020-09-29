class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} приелемая'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} приелемая'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = SportCar(95, 'желтая', 'audi', False)
print(audi.stop())
print(audi.show_speed())
volvo = TownCar(40, 'зеленая', 'volvo', False)
print(volvo.turn_right())
print(volvo.show_speed())
bmw = WorkCar(90, 'черная', 'bmw', False)
print(bmw.turn_left())
print(bmw.show_speed())
print(bmw.name, bmw.color)
print(f'{bmw.name} полицейская машина? {bmw.is_police}')
ford = PoliceCar(105, 'черная',  'ford', True)
print(f'{ford.name} полицейская машина? {ford.is_police}')
print(ford.show_speed())