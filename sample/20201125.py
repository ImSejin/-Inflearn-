# 11. 튜플을 배워보자

# variable = (value1, value2, value3, ...,  valueN)
# 소괄호를 생략할 수 있음

# Packing
ints = 1, 2, 3, 4, 5
print(ints)

# Immutable => modification method가 없음 ... List에 비해 성능상 이점 있음
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

# 12. 리스트를 배워보자

scores = [85, 92, 98, 71]
scores[-1] = 88  # Mutable
scores.append(90)
scores.remove(85)
scores.insert(0, 57)

print(scores)
print('pop: ', scores.pop())
print('pop: ', scores.pop(0))
scores.sort(reverse=True)
print(scores)
scores.clear()
print(scores)

# 13. 리스트 자르기를 배워보자

heights = [185, 171, 177, 190]
sliced = heights[1:3]  # [171, 177]
sliced_to_start = heights[1:]  # [171, 177, 190]
sliced_to_end = heights[:3]  # [185, 171, 177]

# Refer a list
clone_heights = heights
print(heights is clone_heights, heights == clone_heights)  # True, True
# Copies a list
clone_heights = heights[:]
print(heights is clone_heights, heights == clone_heights)  # False, True
clone_heights.append(50)
print(heights is clone_heights, heights == clone_heights)  # False, False
# Copies a list with method
new_heights = heights.copy()
print(heights is new_heights, heights == new_heights)  # False, True

# Concatenates lists: returns a new list
merged_heights = heights + clone_heights
print(merged_heights, heights, clone_heights)

# Extends a list with another list: returns that list, not a new list
new_heights.extend(heights)
print(new_heights, heights)

# 14. 중첩 리스트와 리스트 지우기를 배워보자

day1 = [10, 8, 3, 1]
day2 = [5, 2, 3, 1]
day3 = [15, 8, 2, 3]
total_record = [day1, day2, day3]
print(total_record[2][0] == 15)

for daily in total_record:
    for each in daily:
        print('each', each)

del total_record[:]  # == total_record.clear()
print(total_record)

empty_list = list()
print(empty_list is [], empty_list == [])  # False, True
print('empty_list: ', empty_list)
for n in range(0, 10):
    empty_list.append(n)

print('empty_list: ', empty_list)
