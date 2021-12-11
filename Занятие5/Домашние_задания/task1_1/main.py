def func_add(adder: int = 1, base: int =1) -> int:
    return adder + base


def decorator(fn):
    def wrapper(*args):
        print('wrapper_1')
        result = fn(*args)
        return result
    return wrapper


if __name__ == "__main__":
    # Write your solution here
    dec_f = decorator(func_add)

    print(dec_f(1,2))
