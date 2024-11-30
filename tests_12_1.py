# Домашнее задание по теме "Простые Юнит-Тесты"

# Импортируем модуль runner для его тестирования
import runner
# Импортируем модуль unittest для тестирования кода
import unittest

# Класс RunnerTest наследуется от unittest.TestCase для создания тестов
class RunnerTest(unittest.TestCase):
    # Тест метода walk
    def test_walk(self):
        # Создание нового объекта Runner с именем "Олег"
        runn = runner.Runner("Олег")
        # Цикл для вызова метода walk 10 раз
        for _ in range(10):
            # Вызов метода walk
            runn.walk()
        # Сравнение расстояния пройденного объектом с ожидаемым результатом (50)
        self.assertEqual(runn.distance, 50)

    # Тест метода run
    def test_run(self):
        # Создание нового объекта Runner с именем "Пётр"
        runn = runner.Runner("Пётр")
        # Цикл для вызова метода run 10 раз
        for _ in range(10):
            # Вызов метода run
            runn.run()
        # Сравнение расстояния пройденного объектом с ожидаемым результатом (100)
        self.assertEqual(runn.distance, 100)

    # Тест для проверки поведения двух разных объектов Runner
    def test_challenge(self):
        # Создание двух новых объектов Runner с именами "Никита" и "Алиса"
        runn1 = runner.Runner("Никита")
        runn2 = runner.Runner("Алиса")
        # Цикл для одновременного вызова методов run и walk у двух объектов по 10 раз
        for _ in range(10):
            # Вызов метода run для Никита
            runn1.run()
            # Вызов метода walk для Алиса
            runn2.walk()
        # Проверка того, что дистанции пройденные двумя объектами различны
        self.assertNotEqual(runn1.distance, runn2.distance)

# Запуск тестов, если файл запущен напрямую
if __name__ == "__main__":
    # Запуск всех тестов в текущем файле
    unittest.main()