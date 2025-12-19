import unittest
from test_cd_library import TestCDLibrarySystem

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCDLibrarySystem)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print(f"\n{'='*70}")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    if result.wasSuccessful():
        print("Все тесты пройдены успешно!")