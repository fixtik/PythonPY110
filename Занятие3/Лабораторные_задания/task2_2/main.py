import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename, "r") as ifile, open(output_filename, 'w') as ofile:
        json.dump(json.load(ifile), ofile, indent=4)



if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
