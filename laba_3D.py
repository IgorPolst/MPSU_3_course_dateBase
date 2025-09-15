class Vehicle:
    def __init__(self, make: str, max_speed: int):
        self.make: str = make
        self.max_speed: int = max_speed

    def info(self) -> str:
        res: str  = f"Марка: {self.make}\n"
        res +=f"Максимальная скорость: {self.max_speed}\n"

        return res


class Car(Vehicle):

    def __init__(self, make: str, max_speed: int, passenger_seats: int):
        super().__init__(make, max_speed)
        self.passenger_seats = passenger_seats

    def info(self) -> str:
        res = super().info()
        res += f"Количество пассажирских мест: {self.passenger_seats}\n"
        return res
            
class Train(Vehicle):
    
    def __init__(self, make: str, max_speed:int, carriages_count: int):
        super().__init__(make, max_speed)
        self.carriages_count: int = carriages_count

    def info(self) -> str:
        res: str = super().info()
        res += f"Количество вагонов: {self.carriages_count}\n"
        return res
    