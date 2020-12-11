"""
20. 제어문과 조합하여 만드는 데이터
"""


def get_squares(stop):
    squares = []
    for n in range(1, stop):
        squares.append(n ** 2)

    return squares


# List Comprehension
def get_new_squares(stop):
    return [n ** 2 for n in range(1, stop)]


print('get_squares\t\t\t', get_squares(11) == get_new_squares(11), get_squares(11))  # True


# ---


def rock_paper_scissors():
    __items = 'Rock', 'Paper', 'Scissors'
    result = []
    for a in __items:
        for b in __items:
            if a != b:
                result.append((a, b))

    return result


# Nested LC
def new_rock_paper_scissors():
    __items = 'Rock', 'Paper', 'Scissors'
    return [(a, b) for a in __items for b in __items if a != b]
    # return [(a, b) for a in __items if a == 'Rock' for b in __items if a != b]


print('rock_paper_scissors\t', rock_paper_scissors() == new_rock_paper_scissors(), rock_paper_scissors())  # True


# ---


def get_not_abc():
    x = set()
    for char in 'abracadabra':
        if char not in 'abc':
            x.add(char)

    return x


# Set Comprehension
def get_new_not_abc():
    return {char for char in 'abracadabra' if char not in 'abc'}


print('get_not_abc\t\t\t', get_not_abc() == get_new_not_abc(), get_not_abc())  # True


# ---


def get_squared_dict(stop):
    __squares = {}
    for i in range(1, stop):
        __squares[i] = i ** 2

    return __squares


# Dictionary Comprehension
def get_new_squared_dict(stop):
    return {i: i ** 2 for i in range(1, stop)}


print('get_squared_dict\t', get_squared_dict(11) == get_new_squared_dict(11), get_squared_dict(11))  # True
