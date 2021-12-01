import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    return sorted(json_data, key=lambda x: x['length'])


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    with open('outputfile.json', 'w') as f:
        json.dump(task(), f)

