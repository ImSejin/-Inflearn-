"""
18. 클래스를 만들어 보자
"""


class BookReader:
    name = ''

    def read_book(self):
        print(self.name, '은(는) 책을 읽는다.')


reader = BookReader()
reader.name = '세진'
reader.read_book()

# ---


class NewBookReader:
    def __init__(self, name):
        self.name = name

    def read_book(self):
        print(self.name, '은(는) 책을 읽는다.')


new_reader = NewBookReader('임세진')
new_reader.read_book()
