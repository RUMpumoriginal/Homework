def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is not None:
            end_result = str(result).upper()
        else:
            end_result = result
        
        print(end_result)

        return result
    return wrapper

def positive_only(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            return ValueError("Від'ємне число!!!")
        else:
            print(result)
        
        return result
    return wrapper


@shout
def add_suffix(value):
    return f"{value}suffix"

@positive_only
def add_two(value):
    return value + 2
