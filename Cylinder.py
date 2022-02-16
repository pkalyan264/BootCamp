import math


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        pi = math.pi
        return 2 * pi * self.radius * (self.radius + self.height)

    def volume(self):
        pi = math.pi
        return pi * self.radius ** 2 * self.height


c1 = Cylinder(1, 1)
print(c1.volume())
print(c1.surface_area())