

def fabric_decorator(arg_dec: int):
    def decorator(fn):
        def wrapper(*args):
            result = 0
            for _ in range(arg_dec):
                result += fn(*args)
            return result / arg_dec
        return wrapper
    return decorator

@fabric_decorator(4)
def func_add(adder: int = 1, base: int =1) -> int:
    return adder + base

if __name__ == "__main__":
    # Write your solution here
    print(func_add(2,2))
