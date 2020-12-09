"""
구구단 클래스
"""


class MultiplicationTable:
    def __init__(self, max_multiply):
        self.max_multiply = max_multiply

    def print(self):
        for m in range(1, self.max_multiply + 1):
            for n in range(1, 10):
                print(f'{m} * {n} = {m * n}')

            print('-' * 12)
