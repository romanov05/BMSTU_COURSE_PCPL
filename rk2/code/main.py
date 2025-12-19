from operator import itemgetter

# CD-диск
class CD:
    def __init__(self, id, title, capacity, lib_id):
        self.id = id
        self.title = title
        self.capacity = capacity    # объем в МБ
        self.lib_id = lib_id

# Библиотека CD-дисков
class CDLibrary:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# CD-диски в библиотеках для реализации связи многие-ко-многим
class CD_CDLibrary:
    def __init__(self, lib_id, cd_id):
        self.lib_id = lib_id
        self.cd_id = cd_id


class CDLibrarySystem:
    def __init__(self, libraries, cds, cds_libraries):
        self.libraries = libraries
        self.cds = cds
        self.cds_libraries = cds_libraries
        self.one_to_many = None
        self.many_to_many = None
        self._prepare_data()
    
    def _prepare_data(self):
        # Соединение данных один-ко-многим
        self.one_to_many = [(cd.title, cd.capacity, lib.name)
                           for lib in self.libraries
                           for cd in self.cds
                           if cd.lib_id == lib.id]
        
        # Соединение данных многие-ко-многим
        many_to_many_temp = [(lib.name, cl.lib_id, cl.cd_id)
                            for lib in self.libraries
                            for cl in self.cds_libraries
                            if lib.id == cl.lib_id]
        
        self.many_to_many = [(cd.title, cd.capacity, lib_name)
                            for lib_name, _, cd_id in many_to_many_temp
                            for cd in self.cds if cd.id == cd_id]
    
    def get_libraries_with_name_containing(self, search_term):
        """Задание Е1: Библиотеки, содержащие search_term в названии, с их CD-дисками"""
        result = {}
        for lib in self.libraries:
            if search_term in lib.name:
                lib_cds = list(filter(lambda i: i[2] == lib.name, self.one_to_many))
                lib_cds_titles = [x for x, _, _ in lib_cds]
                result[lib.name] = lib_cds_titles
        return result
    
    def get_avg_capacity_by_library(self):
        """Задание Е2: Библиотеки со средней емкостью CD-дисков, отсортированные по средней емкости"""
        result_unsorted = []
        for lib in self.libraries:
            lib_cds = list(filter(lambda i: i[2] == lib.name, self.one_to_many))
            if len(lib_cds) > 0:
                lib_capacities = [capacity for _, capacity, _ in lib_cds]
                lib_avg_capacity = round(sum(lib_capacities) / len(lib_capacities), 2)
                result_unsorted.append((lib.name, lib_avg_capacity))
        
        # Сортировка по средней емкости
        return sorted(result_unsorted, key=itemgetter(1))
    
    def get_cds_starting_with_letter(self, letter):
        """Задание Е3: CD-диски, название которых начинается с заданной буквы"""
        filtered_cds = list(filter(lambda i: i[0].startswith(letter), self.many_to_many))
        # Сортировка по названию CD-диска
        return sorted(filtered_cds, key=itemgetter(0))

def create_sample_data():
    """Создание тестовых данных"""
    # Библиотеки CD-дисков
    libraries = [
        CDLibrary(1, 'библиотека мультимедиа'),
        CDLibrary(2, 'архив программного обеспечения'),
        CDLibrary(3, 'библиотека фильмов'),
        CDLibrary(4, 'основной архив'),
        CDLibrary(5, 'коллекция литературы'),
        CDLibrary(6, 'библиотека игр'),
    ]
    
    # CD-диски
    cds = [
        CD(11, 'Альбом Rock', 700, 1),
        CD(22, 'Мастер и Маргарита', 650, 5),
        CD(33, 'Фильм "Гарри Поттер и Орден Феникса"', 900, 3),
        CD(44, 'Minecraft', 700, 6),
        CD(55, 'Antivirus Pro', 500, 2),
        CD(66, 'Microsoft Office', 650, 4),
    ]
    
    # Связи многие-ко-многим
    cds_libraries = [
        CD_CDLibrary(1, 11),
        CD_CDLibrary(1, 22),
        CD_CDLibrary(1, 33),
        CD_CDLibrary(2, 44),
        CD_CDLibrary(2, 55),
        CD_CDLibrary(2, 66),
        CD_CDLibrary(3, 33),
        CD_CDLibrary(4, 55),
        CD_CDLibrary(4, 66),
        CD_CDLibrary(5, 22),
        CD_CDLibrary(6, 44)
    ]
    
    return libraries, cds, cds_libraries

def main():
    libraries, cds, cds_libraries = create_sample_data()
    system = CDLibrarySystem(libraries, cds, cds_libraries)
    
    print('Задание Е1')
    res_e1 = system.get_libraries_with_name_containing('библиотека')
    print(res_e1)
    
    print('\nЗадание Е2')
    res_e2 = system.get_avg_capacity_by_library()
    print(res_e2)
    
    print('\nЗадание Е3')
    res_e3 = system.get_cds_starting_with_letter('Ф')
    print(res_e3)

if __name__ == '__main__':
    main()