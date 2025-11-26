import pytest
from main import Person, Student, Teacher, AdminStaff

def test_person_display():
    p = Person("Иван", 30)
    assert p.display_info() == "Person: name=Иван, age=30"

def test_student_display():
    s = Student("Алиса", 19, "IS-23", 3.7)
    assert s.display_info() == "Student: name=Алиса, age=19, group=IS-23, gpa=3.7"

def test_teacher_display():
    t = Teacher("Борис", 45, "Информатика", 20)
    assert t.display_info() == "Teacher: name=Борис, age=45, subject=Информатика, experience=20 years"

def test_adminstaff_display():
    a = AdminStaff("Виктория", 35, "Секретарь", "Приёмная")
    assert a.display_info() == "AdminStaff: name=Виктория, age=35, position=Секретарь, department=Приёмная"

def test_polymorphism():
    people = [
        Person("Иван", 30),
        Student("Алиса", 19, "IS-23", 3.7),
        Teacher("Борис", 45, "Информатика", 20),
        AdminStaff("Виктория", 35, "Секретарь", "Приёмная")
    ]

    results = [p.display_info() for p in people]

    assert isinstance(results[0], str)
    assert isinstance(results[1], str)
    assert isinstance(results[2], str)
    assert isinstance(results[3], str)
