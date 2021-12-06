import random



# ДОП ЗАДАНИЕ 1
# Написать декоратор, сохраняющий результат в файл output.txt помимо возвращения.
# Результаты должны накапливаться в файле.



def my_decorator(fn):
    def wrapper(*args, file_name='output.txt'):
        result = fn(*args)
        with open(file_name, 'a') as ofile:
            ofile.write(str(result))
        return result
    return wrapper

#ДОП ЗАДАНИЕ 2
# Написать генератор, возвращающий по 3 символа из
# текстового файла, при этом не загружая в память весь файл.

def get_count_symbols(file_name: str, count: int = 3, position: int = 0) -> str:
    with open(file_name,'r') as f:
        f.seek(position)
        while f:
            yield f.read(count)

#ДОП ЗАДАНИЕ 3
# Написать генератор, возвращающий по одному слову текстового файла,
# при этом не загружая в память весь файл.
# В качестве разделителя слов использовать символ пробела.

def get_words_from_file(file_name: str, separator=' ') -> str:
    with open(file_name,'r') as f:
        while f:
            line = str.split(f.readline(), sep=separator)
            iter_line = iter(line)
            i = 0
            while i < len(line):
                yield next(iter_line)
                i += 1

#ДОП ЗАДАНИЕ 4
# Написать генератор, возвращающий по одной
# строке из текстового файла. Символом окончания строки является символ “\n”.
# Встроенной реализацией пользоваться нельзя.
# with open(filename) as f:
# for line in f:
def get_lines_from_file(file_name: str) -> str:
    with open(file_name,'r') as f:
        while f:
            yield f.readline()

#ДОП ЗАДАНИЕ 5
# Написать генератор, возвращающий  последние n строк из текстового файла,
# при этом не загружая в память весь файл.
def get_last_lines_from_file(file_name: str, count_lines: int = 3):
    with open(file_name) as f:
        #начало count_lines последний строки
        n, i = 100, count_lines
        eof = f.seek(0, 2)
        while i:
            if eof - n >= 0:
                f.seek(eof - n)
            else:
                f.seek(0)
            try:
                string_read = f.readlines()
                if i+1 - len(string_read) > 0:
                    n += 100
                else:
                    string_read = string_read[-i:]
                    i -= len(string_read)
            except:
                n -= 1 #в случае ошибки декодирования слдвигаемся вправо на 1
    last_lines = iter(string_read)
    for _ in range(len(string_read)):
        yield next(last_lines)


def generator_file(file_name: str, list_len=10):
    with open(file_name, 'w') as ofile:
        ofile.write(','.join([str(random.randint(-100, 100)) for _ in range(0, list_len)]))

#доп задание 1
@my_decorator
def reader_file(file_name1, file_name2: str) -> list:
    with open(file_name1,'r') as f1, open(file_name2, 'r') as f2:
         data_str = (f1.read() +',' + f2.read()).split(',')
    return [int(i) for i in data_str]

if __name__ == "__main__":
    # Write your solution here
    fn1 = "input_file1.txt"
    fn2 = "input_file2.txt"
    task3 ="text_file.txt"

    generator_file(fn1)
    generator_file(fn2)

    print(f"{'-'*5} Задание 1 {'-'*5}".rjust(25,'-'))
    print(reader_file(fn1, fn2))

# #Доп задание 2
    print(f"\n{'-' * 5} Доп задание 2 {'-' * 5}")
    get_symbol = get_count_symbols(fn1)
    print(next(get_symbol))

# #Доп задание 3
    print(f"\n{'-' * 5} Доп задание 3 {'-' * 5}")
    iter_file = get_words_from_file(task3)
    for _ in range(10):
        print(next(iter_file))

# #Доп задание 4
    print(f"\n{'-' * 5} Доп задание 4 {'-' * 5}")
    iter_file_line = get_lines_from_file(task3)
    for _ in range(5):
        print(next(iter_file_line), end='')

#Доп задание 5
    print(f"\n{'-' * 5} Доп задание 5 {'-' * 5}")
    iter_file_line_from_end = get_last_lines_from_file(task3, count_lines=5)
    for _ in range(5):
        print(next(iter_file_line_from_end), end='')