# Conditional statement
x = 'py'
y = 31
if y > 30:
    print(x)
else:
    print(x + 'thon')

# For iteration
for i in [0, 1, 2, 3, 4]:
    print('for:', i)

# While iteration
i = 0
while i < 5:
    print('while:', i)
    i += 1


# Define function
def print_nums(start, end):
    if start > end:
        return

    while start < end:
        print('while:', start)
        start += 1


print_nums(0, 5)
