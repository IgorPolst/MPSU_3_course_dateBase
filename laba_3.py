class Shape:
    
    def square(self) -> float:
        pass
    
    def __str__(self) -> str:
        return f"Данный класс не имеет собственных объектов и является абстрактным"

class Square (Shape):
     
    def __init__(self, side_length: float):
        self.side_length: float = side_length

    def get_side_length(self) -> float:
        return self.side_length
    
    def square(self) -> float:
        return self.side_length ** 2

    def __str__(self) -> str:
        res = f"Сторона квадрата: {self.side_length}\n"
        res += f"Площадь квадрата: {self.square()}\n\n"
        return res


class Triangle(Shape):
    
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def get_base(self) -> float:
        return self.base
    
    def get_height(self) -> float:
        return self.height
    
    def square(self) -> float:
        return self.height*self.base*0.5

    def __str__(self) -> str:
        res = f"Основание треугольника: {self.base}\n"
        res += f"Высота треугольника: {self.height}\n"
        res += f"Площадь треугольника: {self.square()}\n\n"
        return res

