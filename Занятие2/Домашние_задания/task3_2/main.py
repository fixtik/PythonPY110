def task_decorator(fn):
    def wrapper(*args):
        if list(filter(lambda x: type(x) != int, args)):
            raise ValueError('Не все значения целочисленные')
        result = fn(*args)
        return result
    return wrapper

@task_decorator
def my_func(*args):
    return sum(args)

if __name__ == "__main__":
    # Write your solution here

    print(my_func(1,'2',3,4))