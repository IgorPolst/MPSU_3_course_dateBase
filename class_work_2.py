class Teacher:
    def __init__(self, name):
        self.name: str = name

    def __str__(self) -> str:
        return self.name
    
class Student:
    def __init__(self, name):
        self.name: str = name
    def __str__(self):
        return self.name
    
class Group:
    def __init__(self, name):
        self.name: str = name
        self.students : list[Student] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def remove_student(self, student: Student) -> None:
        if student in self.students:
            self.students.remove(student)

    def count_of_student(self) -> int:
        return len(self.students)
    
    def get_student(self, index: int) -> Student:
        if 0<= index <= len(self.students):
            return self.students[index]
        else:
            return IndexError
    def get_students(self) -> list[Student]:
        return self.students
    
    def __str__(self) -> str:
        return self.name
    
class Course:
    def __init__(self, name):
        self.name: str = name
        self.teachers: list[Teacher] = []
        self.groups: list[Group] = []
    
    def add_group(self, group: Group) -> None:
        self.groups.append(group)

    def add_teacher(self, teacher: Teacher) -> None:
        self.teachers.append(teacher)

    def remove_group(self, group: Group) -> None:
        if group in self.groups:
            self.groups.remove(group)

    def remove_teacher(self, teacher: Teacher) -> None:
        if teacher in self.teachers:
            self.teachers.remove(teacher)

    def get_groups(self) -> list[Group]:
        return self.groups
    
    def get_teachers(self) -> list[Teacher]:
        return self.teachers

    def __str__(self) -> str:
        return self.name

def main():
    pass

if __name__ == "__main__":
    main()