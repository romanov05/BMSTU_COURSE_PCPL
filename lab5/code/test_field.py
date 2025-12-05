import unittest
from field import field

class TestFieldGenerator(unittest.TestCase):
    '''TDD тесты для генератора field'''
    
    def test_for_one_field(self):
        '''Тест 1: Возвращаем значения для одного поля'''
        goods = [{'title': 'Ковер', 'price': 2000},
                 {'title': 'Диван', 'price': 3000},
                 {'title': None, 'price': 1000}]
        result = list(field(goods, 'title'))
        expected = ['Ковер', 'Диван']
        self.assertEqual(result, expected)
    
    def test_for_two_fields(self):
        '''Тест 2: Возвращаем значения для двух полей'''
        goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
                 {'title': 'Диван', 'color': 'black'},
                 {'price': 1000, 'color': 'white'}]
        result = list(field(goods, 'title', 'price'))
        expected = [{'title': 'Ковер', 'price': 2000},
                    {'title': 'Диван'},
                    {'price': 1000}]
        self.assertEqual(result, expected)
    
    def test_for_none_fields(self):
        '''Тест 3: None значения правильно фильтруются'''
        goods = [{'title': None, 'price': 100},
                 {'title': 'Шкаф', 'price': None},
                 {'title': None, 'price': None}]
        result = list(field(goods, 'title', 'price'))
        expected = [{'price': 100},
                    {'title': 'Шкаф'}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()