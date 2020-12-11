"""
21. 숫자 맞추기 게임 만들기
"""
import random as rd


class GuessingNumber:
    def __init__(self, start: int, limit: int = 3):
        self.start = start
        self.limit = limit

    @staticmethod
    def __parse_int(string: str):
        __doc__ = """
        To define a private method, add the prefix with double underscore(__) to the member name.
        Also To define a protected method, add the prefix with single underscore(_) to the member name.
        """

        __result = []
        for char in string.strip():
            code_point = ord(char)
            if code_point < 48 or code_point > 57:
                return int(''.join(__result))

            __result.append(char)

        return int(''.join(__result))

    def play(self):
        # Validates parameter.
        if self.start < 1 or self.limit < 1:
            raise ArithmeticError

        # (10): 0 ~ 9
        num = rd.randrange(self.start)

        tries = 0
        while self.limit != tries:
            tries += 1
            guessed_num = self.__parse_int(input(f"Guess what number I'm thinking({tries}/{self.limit}): "))

            if guessed_num == num:
                print('\tCongratulations, You got it!')
                return
            else:
                print(f"\tIt's {'greater' if num > guessed_num else 'less'} than {guessed_num}")

        print(f'\tFailed to guess my number: {num}')


gn = GuessingNumber(10, 4)
# How to access to private method.
number = gn._GuessingNumber__parse_int('02132dsf')  # 2132
gn.play()
