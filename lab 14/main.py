"""
Lab14 — Тестирование и отладка ПО.
Функции:
- calculate_average(grades)
- determine_grade_letter(avg)
- student_report(name, grades)

Логирование: app.log
"""
import logging
from typing import Iterable, List, Union

# Настройка логирования
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


Number = Union[int, float]


def calculate_average(grades: Iterable[Number]) -> float:
    """
    Вычисляет средний балл по списку оценок.

    Args:
        grades: Итерация числовых оценок (int или float).

    Returns:
        Средний балл, округлённый до 2 знаков после запятой.

    Raises:
        ValueError: если grades пуст или содержит 0 элементов.
        TypeError: если в grades есть элементы не числа.
    """
    # Приведём к списку, чтобы можно было дважды пройтись (len, sum)
    try:
        grades_list: List[Number] = list(grades)
    except TypeError:
        logging.error("Входной параметр не является итерируемым")
        raise TypeError("grades должен быть итерируемым (список/кортеж и т.п.)")

    if not grades_list:
        logging.error("Список оценок пуст")
        raise ValueError("Список оценок не может быть пустым")

    if not all(isinstance(x, (int, float)) for x in grades_list):
        logging.error("Некорректный тип данных в списке оценок: %r", grades_list)
        raise TypeError("Все оценки должны быть числами (int или float)")

    avg = sum(grades_list) / len(grades_list)
    logging.info("Средний балл рассчитан: %s (на %d значениях)", avg, len(grades_list))
    return round(avg, 2)


def determine_grade_letter(avg: Number) -> str:
    """
    Определяет буквенную оценку по среднему баллу.

    Шкала:
        >= 90 -> A
        >= 80 -> B
        >= 70 -> C
        >= 60 -> D
        иначе -> F
    """
    try:
        score = float(avg)
    except (TypeError, ValueError):
        logging.error("Некорректное значение среднего балла: %r", avg)
        raise TypeError("avg должен быть числом")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def student_report(name: str, grades: Iterable[Number]) -> str:
    """
    Формирует текстовый отчёт по студенту.

    Args:
        name: Имя студента.
        grades: Итерация оценок.

    Returns:
        Строка-отчёт.
    """
    if not isinstance(name, str):
        logging.error("Имя студента должно быть строкой: %r", name)
        raise TypeError("name должен быть строкой")

    avg = calculate_average(grades)
    letter = determine_grade_letter(avg)
    result = (
        f"Студент: {name}\n"
        f"Средний балл: {avg}\n"
        f"Оценка: {letter}"
    )
    logging.info("Создан отчёт для студента %s: %s", name, letter)
    return result


if __name__ == "__main__":
    # Простой CLI-интерфейс для ручного запуска
    try:
        name = input("Введите имя студента: ").strip()
        if not name:
            raise ValueError("Имя не может быть пустым")

        grades_input = input("Введите оценки через пробел (например: 90 80 100): ").strip()
        if not grades_input:
            raise ValueError("Нужно ввести хотя бы одну оценку")

        # преобразуем ввод в float; если пользователь ввёл нечисло — будет ValueError
        grades = [float(x) for x in grades_input.split()]

        print("\n---- Итоговый отчёт ----")
        print(student_report(name, grades))
    except Exception as e:
        print("Ошибка:", e)
        logging.exception("Произошло исключение при запуске программы")