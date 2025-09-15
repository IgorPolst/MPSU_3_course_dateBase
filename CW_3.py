class GeometicFigure
    def __init__ (self, center: tuple[int, int] = [0,0]):
        self.center = center

    def get_center(self) -> tuple[int, int]:
        return self.center

    def move_on(self, motion: tuple[int, int]) -> None:
        if motion:
            self.center = (self.center[0] + motion[0], self.center[1] + motion[1])

    def __str__ (self):
        return f"{self.__class__, __name__} at {self.center}"
    
    class Circle(GeometicFigure):
        def __init__(self, center: tuple[int, int] = [0,0], radius: int = 0):
            super().__init__(center)
            self.redius = radius

        def get_radius(self) -> int: 
            return self.redius
        
        def set_radius(self, radius:int) -> None:
            if 
        

