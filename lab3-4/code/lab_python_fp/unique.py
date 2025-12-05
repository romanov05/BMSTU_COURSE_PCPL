from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.unique_elements = set()

    def select_case(self, item):
        if self.ignore_case and isinstance(item, str):
            return item.lower()
        return item

    def __next__(self):
        while True:
            item = next(self.items)
            processed_item = self.select_case(item)
            
            if processed_item not in self.unique_elements:
                self.unique_elements.add(processed_item)
                return item

    def __iter__(self):
        return self

if __name__ == "__main__":
    print("Уникальные элементы в массиве [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]:")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data):
        print(item, end=" ")
    print()

    print("Уникальные элементы в генераторе gen_random(10, 1, 3):")
    data = gen_random(10, 1, 3)
    for item in Unique(data):
        print(item, end=" ")
    print()
    
    print("Уникальные элементы в массиве ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'] с учетом регистра:")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data):
        print(item, end=" ")
    print()
    
    print("Уникальные элементы в массиве ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'] без учета регистра:")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data, ignore_case=True):
        print(item, end=" ")
    print()