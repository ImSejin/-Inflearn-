# 11. 튜플을 배워보자

# variable = (value1, value2, value3, ...,  valueN)
# 소괄호를 생략할 수 있음

# Packing
ints = 1, 2, 3, 4, 5
print(ints)

# Immutable
print(ints[-1])  # 5
print(ints[len(ints) - 1])  # 5
# ints[0] = 2  # TypeError: 'tuple' object does not support item assignment

# Iterable
evens = 0, '2', 4, '6', 8,
for n in evens:
    print(n)

# Unpacking
a, b, c, d, e = evens
print(a, b, c, d, e)
