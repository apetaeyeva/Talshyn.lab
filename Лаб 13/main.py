class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self) -> str:
        return f"Person: name={self.name}, age={self.age}"


class Student(Person):
    def __init__(self, name: str, age: int, group: str, gpa: float):
        super().__init__(name, age)
        self.group = group
        self.gpa = gpa

    def display_info(self) -> str:
        return (f"Student: name={self.name}, age={self.age}, "
                f"group={self.group}, gpa={self.gpa}")


class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str, experience: int):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience

    def display_info(self) -> str:
        return (f"Teacher: name={self.name}, age={self.age}, "
                f"subject={self.subject}, experience={self.experience} years")


class AdminStaff(Person):
    def __init__(self, name: str, age: int, position: str, department: str):
        super().__init__(name, age)
        self.position = position
        self.department = department

    def display_info(self) -> str:
        return (f"AdminStaff: name={self.name}, age={self.age}, "
                f"position={self.position}, department={self.department}")


# -----------------------------------------
# Демонстрация работы (полиморфизм)
# -----------------------------------------
if __name__ == "__main__":
    people = [
        Person("Иван", 30),
        Student("Алиса", 19, "IS-23", 3.7),
        Teacher("Борис", 45, "Информатика", 20),
        AdminStaff("Виктория", 35, "Секретарь", "Приёмная")
    ]

    for p in people:
        print(p.display_info())
