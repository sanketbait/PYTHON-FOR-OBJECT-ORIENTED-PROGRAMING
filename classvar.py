# CLASS VARIABLE
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def calc_circumferance(self):
        return 2 * Circle.pi * self.radius

c = Circle(4)
c1 = Circle(10)
print(c.calc_circumferance())
print(Circle.calc_circumferance(c1))
print(c1.calc_circumferance())