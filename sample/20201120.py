# if문 안에서 생성한 변수를 그 밖에서 사용할 수 있다...?
if 1 == 1:
    string = """
        Use of double quotation in multiline string is 
        one of python conventions. 
    """
print(string)

# Embedded variables
print(__file__, __doc__, __name__, __package__)

# Repeat a string
name = 'Im Sejin'
print((name + '\t' * 3) * 3)

# Interpolation (f string)
f_string = f'{name} is a human.'
print(f_string)

# len(Enumerable): 개수를 구한다.
print(name, ':', len(name))

# Operators
print(2 + 3)  # 5
print(2 - 3)  # -1
print(2 * 3)  # 6
print(2 / 3, 4 / 2)  # 0.6666666666666666, 2.0: 나누기 연산은 무조건 실수형을 반환?
print(5 // 2)  # 2
print(5 % 2)  # 1
print((5 & 1 == 1) is True)  # True: boolean 타입 비교는 '=='보다 'is'로 하는 게 좋다.
print(2 ** -3)  # 2^-3 = 1/2^3 = 1/8 = 0.125
print(3 ** 0.5)  # 3^(1/2) = √3 = 1.7320508075688772
print(2 ** -0.5)  # 2^-(1/2) = 1/√2 = 0.7071067811865476

# input(String): 콘솔의 표준입력을 받는다.
num = input('\nInput your number')

# Convert string to integer
num = int(num)
print(num * 2)

# Convert integer to string
num = str(num)
print(num * 2)
