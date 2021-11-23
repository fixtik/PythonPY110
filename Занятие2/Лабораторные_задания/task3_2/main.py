def min_len_check(fn):
    def wrapper(arg):
        if len(arg) < 10:
            raise ValueError("Строка слишком короткая")
        result = fn(arg)
        return result
    return wrapper


@min_len_check
def some_func(str_arg: str):
    print(str_arg)


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
