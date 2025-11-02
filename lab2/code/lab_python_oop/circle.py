from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math

class Circle(Figure):
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, radius):
        self.radius = radius
        self.figure_color = Color()
        self.figure_color.color = color

    def square(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return f'{Circle.get_figure_type()} {self.figure_color.color} цвета ' \
               f'радиусом {self.radius} площадью {self.square()}.'