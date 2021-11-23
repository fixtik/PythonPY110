import random
from string import ascii_lowercase, ascii_uppercase, digits

def pass_gen(*args, length: int):
    population = []
    for _, value in enumerate(args):
        population += value
    while True:
        yield random.sample(population, length)

if __name__ == "__main__":
    print(ascii_lowercase)
    print(ascii_uppercase)
    print(digits)

    passwd = pass_gen(ascii_lowercase,ascii_uppercase, digits, length=8)
    print(''.join(next(passwd)))
