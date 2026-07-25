def log_args(func):
    def wrapper(*args):
        print(*args)
        return func(*args)
    return wrapper


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


def walrus_operator(dict: dict):
    _list = list(dict.items())
    for i in range(len(dict)):
        if (item := _list[i]) and (value := item[1]) and len(value) >= 4:
            print(value)


def countdown(n):
    while n >= 0:
        if n == 0:
            n = "Start"
        yield n
        n -= 1



