"""
17. 함수를 만들어 보자
"""


def greetings():
    print('Hello World!')


greetings()


def greetings(name):
    print(f'{name}님, 반갑습니다.')


greetings('John')
# greetings()  # Cannot overload.


def add_suffix(name):
    return f'{name}님'


print(add_suffix('Alex'))
