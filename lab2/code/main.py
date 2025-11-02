from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import numpy

def main():
    rectangle = Rectangle("синего", 13, 13)
    circle = Circle("зеленого", 13)
    square = Square("красного", 13)
    print(rectangle)
    print(circle)
    print(square)

    print()

    arr = numpy.array([1, 2, 3, 4, 5])
    average = arr.mean()
    print(f"Массив: {arr}")
    print(f"Среднее значение: {average}")

if __name__ == "__main__":
    main()