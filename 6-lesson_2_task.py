class Road:
    def __init__(self, _length, _width, asphalt_mass, thickness):
        self._length = _length
        self._width = _width
        self.asphalt_mass = asphalt_mass
        self.thickness = thickness

    def mass(self):
        return self._length * self._width * self.asphalt_mass * self.thickness / 1000


class MassCount(Road):
    def __init__(self, _length, _width, asphalt_mass, thickness):
        super().__init__(_length, _width, asphalt_mass, thickness)


r = MassCount(20, 5000, 25, 5)
print(r.mass())