from time import time, sleep
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time()
        return self
    
    def __exit__(self, type, value, traceback):
        self.end_time = time()
        work_time = self.end_time - self.start_time
        print(f'time: {work_time:.1f}')

@contextmanager
def cm_timer_2():
    start_time = time()
    yield
    end_time = time()
    work_time = end_time - start_time
    print(f'time: {work_time:.1f}')

if __name__ == "__main__":
    print("Тест cm_timer_1:")
    with cm_timer_1():
        sleep(5.5)

    print("Тест cm_timer_2:")
    with cm_timer_2():
        sleep(3.3)

