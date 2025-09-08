class MenuItem:
    def __init__(self, name: str, price: int, calories: int):
        self.name: str = name
        self.price: int = price
        self.calories: int = calories

    def __str__(self) -> str:
        result : str = f"{self.name}: "
        result += f"Цена: {self.price} "
        result += f"Калории: {self.calories}\n"
        return result

class Cafe:
    def __init__(self, name: str, count_places: int):
        self.name: str = name
        self.count_places: int = count_places
        self.menu: list[MenuItem] = []

    def add_menu_item(self, item: MenuItem) -> None:
        self.menu.append(item)

    def remove_menu_item(self, item:MenuItem) -> None:
        if item in self.menu:
            self.menu.remove(item)

    def get_menu_item(self, index: int) -> MenuItem:
        if 0 <= index <= len(self.menu):
            return self.menu[index]
        else:
            return IndexError
        
    def get_menu_size(self) -> int:
        return len(self.menu)
        
    def get_menu_description(self) -> str:
        result: str = str()

        for item in self.menu:
            result += str(item)
        
        return result
    
    def __str__(self) -> str:
        return self.name


class Order:
    def __init__(self, date: str = str(), order_dishes:MenuItem = [], total_price: int = 0):
        self.date: str = date
        self.ordered_dishes: list[MenuItem] = order_dishes
        self.total_price: int = total_price

    def add_menu_item(self, item: MenuItem) -> None:
        self.ordered_dishes.append(item)
        self.total_price = 0

    def remove_menu_item(self, item:MenuItem) -> None:
        if item in self.ordered_dishes:
            self.ordered_dishes.remove(item)
        
        self.total_price = 0

    def get_menu_item(self, index: int) -> MenuItem:
        if 0 <= index < len(self.ordered_dishes):
            return self.ordered_dishes[index]
        else:
            return IndexError
        
    def get_menu_size(self) -> int:
        return len(self.ordered_dishes)
        
    def calculate_price(self) -> None:
        self.total_price = 0

        for item in self.ordered_dishes:
            self.total_price += item.price


    def print_ordered_dishes(self) -> None:
        result: str = str()

        for item in self.ordered_dishes:
            result += str(item)
        
        return result

    def __str__(self) -> str:
        result: str = f"{self.data}, "
        result += f"Цена: {self.total_price}"
        return result             
    
def main():
    it1 = MenuItem("Яичница", 150, 80)
    it2 = MenuItem("Гречка", 300, 100)
    it3 = MenuItem("Омлет", 200, 70)

    print(it1)

    cafe: Cafe = Cafe("Брусника", 100)
    cafe.add_menu_item(it1)
    cafe.add_menu_item(it2)
    cafe.add_menu_item(it3)

    print(cafe)
    print(cafe.get_menu_description())

    order = Order("08_09_2025")
    order.add_menu_item(it2)
    order.add_menu_item(it3)
    order.calculate_price()

    print(order)
    print(order.print_ordered_dishes())

if __name__ == "__main__":
    main()