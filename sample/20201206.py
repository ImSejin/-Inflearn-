"""
18. 클래스를 만들어 보자
"""


class BookReader:
    # 모든 인스턴스들이 같은 값으로 초기화되는 변수(클래스 변수)
    name = ''

    def read_book(self):
        print(self.name, '은(는) 책을 읽는다.')


reader = BookReader()
reader.name = '세진'
reader.read_book()
print(BookReader().name)


# ---


class NewBookReader:
    # '__init__'은 생성자
    def __init__(self, name):
        # 각 인스턴스가 고유하게 가지는 변수(인스턴스 변수)
        self.name = name

    def read_book(self):
        print(self.name, '은(는) 책을 읽는다.')


new_reader = NewBookReader('임세진')
new_reader.read_book()
