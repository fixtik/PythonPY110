import re

pattern = r'\"{3}\s?(.+\n?.+)\"{3}'
FILE_NAME = 'input.txt'

def without_regex():
    with open(FILE_NAME) as f:
        input_data = str.split(f.read(), sep='\"\"\"')
    for item in input_data:
        if len(item) > 2:
            print('-' * 10, '\n', item)
    print('-'*10)

def with_regex():
    p = re.compile(pattern, re.S)
    with open(FILE_NAME) as f:
        result = re.findall(pattern, f.read())
    for qoute in result:
        print(qoute, '\n', '-'*10)


if __name__ == "__main__":


    without_regex()

    with_regex()



