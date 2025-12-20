def NULL_not_found(object: any) -> int:
    if object is None:
        name = "Nothing"
    elif isinstance(object, float) and object != object:
        name = "Cheese"
    elif object is False:
        name = "Fake"
    elif isinstance(object, int) and object == 0:
        name = "Zero"
    elif object == "":
        print(f'Empty: {type(object)}')
        return 0
    else:
        print("Type not found")
        return 1

    print(f'{name}: {object} {type(object)}')
    return 0
