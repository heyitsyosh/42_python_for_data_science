import time, datetime

today = datetime.datetime.now()
seconds = time.time()
print(f'Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation')
print(today.strftime("%b %d %Y"))


def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(f'{object} is in the kitchen : {type(object)}')
    elif isinstance(object, (list, tuple, set, dict)):
        type_name = object.__class__.__name__.capitalize()
        print(f'{type_name} : {type(object)}')
    else:
        print("Type not found")
    return 42
