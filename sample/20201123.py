# 5. 숫자 타입을 배워보자
# 6. 논리 타입과 비교/논리 연산자를 배워보자

# Iterates a string.
for i in 'string':
    print(i)
print()

# Compares a string with another string.
print("'안녕' == '안녕': ", '안녕' == '안녕')
print("'안녕' is '안녕': ", '안녕' is '안녕')  # SyntaxWarning: "is" with a literal. Did you mean "=="?
print('안녕' == ' 안녕')
print('a' < 'aa')
print()

print("None or 'B': ", None or 'B')  # B
print("'' or 'B': ", '' or 'B')  # B
print("'' or 'B': ", ' ' or 'B')  # ' '
print("'A' or 'B': ", 'A' or 'B')  # A
print()

print("None and 'B': ", None and 'B')  # None
print("'' and 'B': ", '' and 'B')  # ''
print("'A' and 'B': ", 'A' and 'B')  # B
print()

# Priority: not > and > or
print(True and False)  # False
print(True or False)  # True
print(not True or False)  # (not True) or False
print(not True and False)  # (not True) and False
print(not True and False or False)  # ((not True) and False) or False
print()

# Converts number and string to boolean.
print(bool(1))  # True
print(bool(0))  # False
print(bool(-0.1))  # True
print(bool(''))  # False
print(bool('False'))  # True
print()

# Short-circuit evaluation.
x = None or 'DEFAULT'
y = '' or 'default'
z = 'value' and None
print(x, y, z)  # DEFAULT default None
print()

# Binary
print(0b0111)  # 7
# Octal
print(0o0111)  # 73
# Hexadecimal
print(0xff)  # 255
# Complex
print(5.4 - 1.3j)
print(complex(5.5, -1.2))

# Checks type.
print(type(0.0))
print(type(0))
print(type(''))
print(type(None))
print(type(True))
print(type(2 + 3j))
print(type(''.split()), type([]))
print(type({}))
print(type(type(0)))

# Splits a string and casting type.
a, b, c = map(int, '1,2,3'.split(','))

# Swaps
c, b, a = a, b, c
print(a, b, c)

# Finalizes variables.
del b, c
print(a)
print()
