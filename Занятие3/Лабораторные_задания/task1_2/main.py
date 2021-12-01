OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, 'w') as f:
        for i in range(1,11):
            f.writelines(f'{"*"*i}\n'.rjust(11))


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
