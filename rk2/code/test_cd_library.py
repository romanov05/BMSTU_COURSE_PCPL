import unittest
from main import CDLibrarySystem, create_sample_data

class TestCDLibrarySystem(unittest.TestCase):
    def setUp(self):
        """Настройка тестовых данных перед каждым тестом"""
        libraries, cds, cds_libraries = create_sample_data()
        self.system = CDLibrarySystem(libraries, cds, cds_libraries)
    
    def test_get_libraries_with_name_containing(self):
        """Тест для задания Е1: поиск библиотек по названию"""
        # Ищем библиотеки, содержащие "библиотека" в названии
        result = self.system.get_libraries_with_name_containing('библиотека')
        
        # Проверяем, что найдены правильные библиотеки
        expected_libraries = {'библиотека мультимедиа', 'библиотека фильмов', 'библиотека игр'}
        self.assertEqual(set(result.keys()), expected_libraries)
        
        # Проверяем количество CD-дисков в библиотеке мультимедиа
        self.assertEqual(len(result['библиотека мультимедиа']), 1)
        
        # Проверяем конкретные CD-диски в библиотеке игр
        self.assertIn('Minecraft', result['библиотека игр'])
    
    def test_get_avg_capacity_by_library(self):
        """Тест для задания Е2: средняя емкость CD-дисков по библиотекам"""
        result = self.system.get_avg_capacity_by_library()
        
        # Проверяем, что результат отсортирован по средней емкости
        capacities = [avg for _, avg in result]
        self.assertEqual(capacities, sorted(capacities))
        
        # Проверяем правильность расчета для библиотеки мультимедиа
        for lib_name, avg_capacity in result:
            if lib_name == 'библиотека мультимедиа':
                self.assertEqual(avg_capacity, 700.0)
                break
        
        # Проверяем, что все библиотеки присутствуют в результате
        self.assertEqual(len(result), 6)
    
    def test_get_cds_starting_with_letter(self):
        """Тест для задания Е3: поиск CD-дисков по начальной букве"""
        # Ищем CD-диски, начинающиеся с 'Ф' (кириллица)
        result = self.system.get_cds_starting_with_letter('Ф')
        
        # Проверяем, что найден правильный CD-диск
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], 'Фильм "Гарри Поттер и Орден Феникса"')
        
        # Проверяем, что результат отсортирован по названию
        titles = [title for title, _, _ in result]
        self.assertEqual(titles, sorted(titles))

if __name__ == '__main__':
    unittest.main(verbosity=2)