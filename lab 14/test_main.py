import unittest
from main import calculate_average, determine_grade_letter, student_report


class TestGrades(unittest.TestCase):
    # Тесты для calculate_average
    def test_average_calculation(self):
        self.assertEqual(calculate_average([90, 80, 100]), 90.0)
        self.assertEqual(calculate_average([70, 75, 80]), 75.0)
        # Проверка округления
        self.assertEqual(calculate_average([90, 91]), 90.5)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_average_type_error(self):
        with self.assertRaises(TypeError):
            calculate_average([90, "80", 70])

    def test_average_non_iterable(self):
        # Передаём неитерируемое значение — ожидаем TypeError
        with self.assertRaises(TypeError):
            calculate_average(123)  # 123 не итерируем

    # Тесты для determine_grade_letter
    def test_letter_grade(self):
        self.assertEqual(determine_grade_letter(95), "A")
        self.assertEqual(determine_grade_letter(90), "A")
        self.assertEqual(determine_grade_letter(89.9), "B")
        self.assertEqual(determine_grade_letter(82), "B")
        self.assertEqual(determine_grade_letter(75), "C")
        self.assertEqual(determine_grade_letter(65), "D")
        self.assertEqual(determine_grade_letter(40), "F")

    def test_letter_type_error(self):
        with self.assertRaises(TypeError):
            determine_grade_letter("ninety")

    # Тесты для student_report
    def test_student_report_content(self):
        res = student_report("Алиса", [100, 90, 80])
        self.assertIn("Алиса", res)
        self.assertIn("Средний балл", res)
        self.assertIn("A", res)

    def test_student_report_invalid_name(self):
        with self.assertRaises(TypeError):
            student_report(123, [90, 80, 70])  # имя не строка


if __name__ == "__main__":
    unittest.main()