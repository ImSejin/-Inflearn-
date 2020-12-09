"""
19. 모듈과 패키지를 만들어 보자
"""
import math

# import custom.multiplication_table
from custom.multiplication_table import MultiplicationTable as Table

pi = math.pi
print(pi)

# table = custom.multiplication_table.MultiplicationTable(9)
table = Table(9)
table.print()
