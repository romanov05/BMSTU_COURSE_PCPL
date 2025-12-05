def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    
    else:
        for item in items:
            result = {}
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
            
            if result:
                yield result

if __name__ == "__main__":
    goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
             {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
             {'title': None, 'price': 7000, 'color': 'red'},
             {'title': 'Шкаф', 'price': None, 'color': 'brown'},
             {'title': None, 'price': None, 'color': None}]
    
    print("Передан один аргумент:")
    for value in field(goods, 'title'):
        print(value)

    print()
    
    print("Передано несколько аргументов:")
    for value in field(goods, 'title', 'price', 'color'):
        print(value)