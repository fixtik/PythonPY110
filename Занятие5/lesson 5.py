import datetime
import random
import time


def task1(lst: list) -> int:
    s = ''
    for i in lst:
        s += str(lst[i])
    return int(s, 2)

print(task1([0, 1, 1, 0, 1, 1, 1]))

def task2(string: str):
    for i in range(len(string)):
        print(string[:i] + string[i].upper() + string[i+1:])

task2('hello')

def task3(string: str):
    while True:
        n = len(string)

        for i in range(n-1):
            yield string[:i] + string[i].upper() + string[i+1:]

        revers = string[::-1]
        for i in range(n):
            if i != n-1:
                yield (revers[:i] + revers[i].upper() + revers[i+1:])[::-1]


gen = task3('word')
for _ in range(10):
    print(next(gen))


def task4(string: str):
    def wowrd_w(word: str):
        summ = 0
        for i in word:
            summ += dict_[i]
        return summ

    list_words = string.split()
    a = ord('а')
    dict_ = {}
    alpha = ''.join([chr(i) for i in range(a,a+32)])
    for indx, value in enumerate(alpha):
        dict_[value] = indx
    return max(list_words, key=wowrd_w)


print(task4("открой сомкнутой негой взоры"))

def task5(string: str) -> str:
    middle = len(string) // 2
    if len(string) % 2:
        left = (string[:middle])[::-1] + string[middle]
        right = (string[middle+1:])[::-1]
    else:
        left = (string[:middle])[::-1]
        right = (string[middle:])[::-1]
    return left + right


print(task5("male"))
print(task5("mouse"))


def task6(rimsk: str):
    dict_ = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
    i, num = 0, 0
    n = len(rimsk)
    while i <= n-1:
        if i+1 <=n - 1:
            if dict_[rimsk[i]] < dict_[rimsk[i+1]]:
                num += (dict_[rimsk[i+1]] - dict_[rimsk[i]])
                i +=2
            else:
                num += dict_[rimsk[i]]
                i += 1
        else:
            num += dict_[rimsk[i]]
            i += 1
    return num

print(task6('MDCLXVI'))


def task7():
    def get_name(length = 3, lang = 'ru') -> str:
        s = ''
        if lang == 'ru':
            alpha = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])
        if lang == 'en':
            alpha = ''.join([chr(i) for i in range(ord('a'), ord('a') + 23)])
        for _ in range(length):
            s += alpha[random.randint(0, len(alpha)-1)]
        return s

    def get_phone_num(region = '+7') -> str:
        def get_gr(len: int) -> str:
            s=''
            for _ in range(len):
                s+= str(random.randint(0,10))
            return s
        numb = f'{region}({get_gr(3)}){get_gr(3)}-{get_gr(2)}-{get_gr(2)}'
        return numb

    def get_datetime() -> str:
        date = datetime.datetime.now()
        return date.isoformat()



    dict_ = {'name': get_name(5).capitalize(),
             'surename': get_name(8).capitalize(),
             'login': '@'+get_name(8, 'en'),
             'password': get_name(12, 'en'),
             'email': get_name(6, 'en')+'@'+get_name(4,'en')+'.'+get_name(3, 'en'),
             'phone': get_phone_num(),
             'register_time': get_datetime()
             }

    print(dict_)


task7()