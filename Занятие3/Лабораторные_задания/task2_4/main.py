import json


def task():
    filename = "input.json"
    with open(filename, 'r') as f:
        json_data = json.load(f)

    gen_exr = (item['contains_improvement_appeals'] for item in json_data)
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
