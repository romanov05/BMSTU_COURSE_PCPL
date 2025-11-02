from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, side):
        self.side = side
        super().__init__(color, self.side, self.side)

    def __repr__(self):
        return f'{Square.get_figure_type()} {self.figure_color.color} цвета ' \
               f'со стороной {self.side} площадью {self.square()}.'