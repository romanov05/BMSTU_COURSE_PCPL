from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, width, height):
        self.width = width
        self.height = height
        self.figure_color = Color()
        self.figure_color.color = color

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return f'{Rectangle.get_figure_type()} {self.figure_color.color} цвета ' \
               f'шириной {self.width} и высотой {self.height} ' \
               f'площадью {self.square()}.'