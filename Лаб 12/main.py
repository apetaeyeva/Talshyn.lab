import json

class Student:
    def __init__(self, name, group, gpa):
        self.__name = name
        self.__group = group
        self.__gpa = gpa

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def get_gpa(self):
        return self.__gpa

    def display_info(self):
        print(f"Имя: {self.__name}, Группа: {self.__group}, Средний балл: {self.__gpa}")

    def update_gpa(self, new_gpa):
        if 0 <= new_gpa <= 4.0:
            self.__gpa = new_gpa
        else:
            print("Ошибка: GPA должен быть от 0 до 4.0")

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if s.get_name() != name]

    def show_all(self):
        if not self.students:
            print("Нет студентов.")
        for s in self.students:
            s.display_info()

    def get_top_students(self, threshold):
        print(f"Студенты с GPA выше {threshold}:")
        for s in self.students:
            if s.get_gpa() > threshold:
                s.display_info()

    def save_to_json(self):
        data = [
            {"name": s.get_name(), "group": s.get_group(), "gpa": s.get_gpa()}
            for s in self.students
        ]
        with open("students.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    group = Group()
    s1 = Student("Акрам", "CS-22", 3.7)
    s2 = Student("Талшын", "CS-22", 2.9)
    s3 = Student("Ринат", "IT-11", 3.95)
    group.add_student(s1)
    group.add_student(s2)
    group.add_student(s3)

    print("\nВсе студенты:")
    group.show_all()

    print("\nОбновляем GPA...")
    s2.update_gpa(3.1)

    print("\nТоп студенты:")
    group.get_top_students(3.0)

    print("\nУдаляем одного студента (Ринат)...")
    group.remove_student("Ринат")

    print("\nПосле удаления:")
    group.show_all()

    group.save_to_json()
    print("\nДанные сохранены в students.json")
