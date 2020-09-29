class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Отрисовка {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Отрисовка ручкой.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Отрисовка карандашом.'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Отрисовка руками.'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Рука')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
