"""
It is a docstring.
16. 딕셔너리를 배워보자
"""

# 딕셔너리 생성
programmers = {'python': 14, 'ruby': 5, 'c++': 10}

# 딕셔너리 값 변경
programmers['python'] -= 1

# 딕셔너리의 키 리스트 타입은 유사 리스트
print(type(programmers.keys()))
keys = list(programmers.keys())

# 딕셔너리의 값 리스트 타입은 유사 리스트
print(type(programmers.values()))
values = list(programmers.values())

# 딕셔너리에 해당 키가 있는지 확인
contains = 'python' in programmers
print(contains, programmers)

# 딕셔너리에서 엔트리를 삭제
del programmers['ruby']
print(programmers)
programmers.clear()
print(programmers)

# 튜플을 딕셔너리로 변환
tuples = ('rust', 8), ('kotlin', 9), ('golang', 6)
dictionary = dict(tuples)
print(tuples, '=>', dictionary)
print(dictionary, '=>', tuple(dictionary))

# 정렬하는 방법
nums = 5, 7, 1, 1, 67, 8, 3, 2, 4, 94
sorted_list = sorted(nums)  # sorted 메서드는 list를 반환한다.
print('Original tuple is not sorted by "sorted()": ', nums)

num_list = [5, 7, 1, 1, 67, 8, 3, 2, 4, 94]
sorted(num_list)
print('Original list is not sorted by "sorted()": ', num_list)
num_list.sort()
print('But original list is sorted by "list.sort()": ', num_list)

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = sorted(x)
x[0][0] = 0
print(x, y)
