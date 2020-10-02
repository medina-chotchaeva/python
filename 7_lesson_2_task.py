class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def coat_square(self):
        return self.width / 6.5 + 0.5

    def jacket_square(self):
        return self.height * 2 + 0.3

    @property
    def full_square(self):
        return str(round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)))


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.coat_square = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return str(self.coat_square)


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.jacket_square = round(self.height * 2 + 0.3)

    def __str__(self):
        return str(self.jacket_square)

coat = Coat(5, 3)
jacket = Jacket(3, 2.4)
print(coat)
print(jacket)
print(coat.full_square)
print(jacket.full_square)
print(int(coat.full_square) + int(jacket.full_square))