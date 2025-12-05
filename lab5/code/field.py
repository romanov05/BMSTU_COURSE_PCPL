def field(items, *args):
    assert len(args) > 0, "Необходимо передать хотя бы одно поле"

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