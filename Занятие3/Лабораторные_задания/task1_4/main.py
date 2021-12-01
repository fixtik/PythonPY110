INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE,"r") as ifile, open(OUTPUT_FILE,'w') as ofile:
        ofile.write(ifile.read().upper())


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
