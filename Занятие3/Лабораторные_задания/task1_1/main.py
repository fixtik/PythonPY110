INPUT_FILE = "input.txt"


def task() -> None:
    with open(INPUT_FILE,'r') as file:  # TODO открыть указатель на файл
        for line in file:
            print(line,end='')


if __name__ == "__main__":
    task()
