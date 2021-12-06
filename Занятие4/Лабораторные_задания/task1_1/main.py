import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = '''\s+(?P<position>\d\d?)\.\s+\[(?P<book>.*?)\]\s?\((?P<book_url>.*?)\)\s?by\s?(?P<author>.*?)\((?P<recommended>\d{,3}\.?\d?).*?\).*?\((?P<cover_url>.*?)\).*?\"(?P<description>.*?)\"''' #


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    json_data = list()
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))
            json_data.append((book.groupdict()))

    json_data.sort(key=lambda dict_e: int(dict_e['position']))

    with open('New.json', 'w') as jf:
        json.dump(json_data, jf, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    task()
