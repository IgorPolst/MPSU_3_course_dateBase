class Human:
# Конструктор       
    def __init__(self, name, age, height): 
        self.name: str = name
        self.age: int = age
        self.height: float = height
    
    def birthday(self):
        self.age += 1

    def __str__(self) -> str:
        return f"Имя:{self.name}\nВозраст:{self.age} \nРост:{self.height}\n"

def main():   
    person = Human("Игорь", 23, 180)
    person.birthday()
    print(person)

if __name__ == "__main__":
    main()

