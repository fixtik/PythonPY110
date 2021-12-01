def task_decorator(fn):
    def wrapper(*args, **kwargs):
        for indx, value in enumerate(args):
            try:
                (_ for _ in value)
            except:
                raise TypeError(
                        f"Объект {type(value)} с позицией {indx} и значением {value} не является итерируемым")
        for key in kwargs:
            try:
                (_ for _ in kwargs[key])
            except:
                raise TypeError(
                    f"Объект {type(kwargs[key])} с ключом {key} и значением {kwargs[key]} не является итерируемым")
        result = fn(*args, **kwargs)
        return result
    return wrapper

@task_decorator
def func(*args, **kwargs):
    print(args, kwargs)


if __name__ == "__main__":

    func('Hello world', '9;', '222', key=1)
