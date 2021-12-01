import json


def task():
    filename = "input.json"
    with open(filename, 'r') as f:
        json_data = json.load(f)

    return max(json_data, key=lambda x: x['score'])


if __name__ == "__main__":
    print(task())
