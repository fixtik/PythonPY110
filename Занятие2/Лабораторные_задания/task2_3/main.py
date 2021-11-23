from itertools import count
def pow_gen(base: int):
    for i in count(0, 1):
        yield base ** i


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
