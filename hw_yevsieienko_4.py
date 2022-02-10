import random

"""
Task 1
Напишите программу для преобразования списка в кортеж
"""

LIST_SIZE = int(input("Enter the number of the list size: "))
RANDOM_UPPER_BOUND = int(input("Enter the number of the upper bound: "))
my_random_list = []

for _ in range(0, LIST_SIZE):
    my_random_list.append(random.randint(0, RANDOM_UPPER_BOUND))
print(f"List: {my_random_list}. Type: {type(my_random_list)}")

my_tuple = tuple(my_random_list)
print(f"Tuple: {my_tuple}. Type: {type(my_tuple)}")

"""
Task 2
Напишите программу для замены последнего значения
кортежей в списке
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

LIST_SIZE_1 = int(input("Enter the number of the list 1 size: "))
RANDOM_UPPER_BOUND_1 = int(input("Enter the number of the upper bound 1: "))
random_list_1 = []

for _ in range(0, LIST_SIZE_1):
    random_list_1.append(random.randint(0, RANDOM_UPPER_BOUND_1))
random_tuple_1 = tuple(random_list_1)
print(f"Tuple 1: {random_tuple_1}")

LIST_SIZE_2 = int(input("Enter the number of the list 2 size: "))
RANDOM_UPPER_BOUND_2 = int(input("Enter the number of the upper bound 2: "))
random_list_2 = []

for _ in range(0, LIST_SIZE_2):
    random_list_2.append(random.randint(0, RANDOM_UPPER_BOUND_2))
random_tuple_2 = tuple(random_list_2)
print(f"Tuple 2: {random_tuple_2}")

LIST_SIZE_3 = int(input("Enter the number of the list 3 size: "))
RANDOM_UPPER_BOUND_3 = int(input("Enter the number of the upper bound 3: "))
random_list_3 = []

for _ in range(0, LIST_SIZE_3):
    random_list_3.append(random.randint(0, RANDOM_UPPER_BOUND_3))
random_tuple_3 = tuple(random_list_3)
print(f"Tuple 3: {random_tuple_3}")

sample_list = [random_tuple_1, random_tuple_2, random_tuple_3]
print(f"Sample list: {sample_list}")

new_sample_list = []
replace_number = int(input("Enter a number that shall replace the last item in each tuple: "))

for i in sample_list:
    new_sample_list.append(list(i))

print(f"Sample list of lists: {new_sample_list}")

for i, sublist in enumerate(new_sample_list):
    for j, item in enumerate(sublist):
        sublist[-1] = replace_number

print(f"Replaced list of lists: {sample_list}")

replaced_sample_tuple = []

for i in new_sample_list:
    replaced_sample_tuple.append(tuple(i))

print(f"Replaced list of tuples: {replaced_sample_tuple}")

"""
Task 3
Напишите программу для поэлементного вычисления суммы
заданных кортежей. Результатом должен быть кортеж.
Input
(1, 2, 3, 4)
(3, 5, 2, 1)
(2, 2, 3, 1)
Output
(6, 9, 8, 6)
"""

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

list1 = list(tuple1)
list2 = list(tuple2)
list3 = list(tuple3)

my_new_list = []

for i, j in enumerate(list1):
    my_new_list.append(list1[i] + list2[i] + list3[i])

my_new_tuple = tuple(my_new_list)

print(my_new_tuple)

"""
Task 4
Напишите программу, которая проверяет, присутствует ли А в
наборе или нет. А вводится с клавиатуры
"""

LIST_SIZE_7 = int(input("Enter the number of the list size: "))
RANDOM_UPPER_BOUND_7 = int(input("Enter the number of the upper bound: "))
random_list_7 = []

for _ in range(0, LIST_SIZE_7):
    random_list_7.append(random.randint(0, RANDOM_UPPER_BOUND_7))

random_set = set(random_list_7)
print(f"Set: {random_set}")

num_a = int(input("Enter any number: "))

if num_a in random_set:
    print("Your number is in set!")
else:
    print("Your number is NOT in set.")

"""
Task 5
Напишите программу, чтобы проверить, не имеют ли два
заданных набора (set) общих элементов.
"""

LIST_SIZE_8 = int(input("Enter the number of the list 1 size: "))
RANDOM_UPPER_BOUND_8 = int(input("Enter the number of the upper bound 1: "))
random_list_8 = []

for _ in range(0, LIST_SIZE_8):
    random_list_8.append(random.randint(0, RANDOM_UPPER_BOUND_8))

set_a = set(random_list_8)
print(f"Set a: {set_a}")

LIST_SIZE_9 = int(input("Enter the number of the list 2 size: "))
RANDOM_UPPER_BOUND_9 = int(input("Enter the number of the upper bound 2: "))
random_list_9 = []

for _ in range(0, LIST_SIZE_9):
    random_list_9.append(random.randint(0, RANDOM_UPPER_BOUND_9))

set_b = set(random_list_9)
print(f"Set b: {set_b}")


inter_set = set_a & set_b

if len(inter_set) == 0:
    print("Your 2 sets have NO common values.")
else:
    print(f"Your 2 sets have the following common value/-s: {inter_set}")

"""
Task 6
Напишите программу для поиска элементов в данном наборе A
(set), которых нет в другом наборе B.
"""

LIST_SIZE_10 = int(input("Enter the number of the set A size: "))
RANDOM_UPPER_BOUND_10 = int(input("Enter the number of the upper bound A: "))
random_list_10 = []

for _ in range(0, LIST_SIZE_10):
    random_list_10.append(random.randint(0, RANDOM_UPPER_BOUND_10))

set_a1 = set(random_list_10)
print(f"Set A: {set_a1}")

LIST_SIZE_11 = int(input("Enter the number of the set B size: "))
RANDOM_UPPER_BOUND_11 = int(input("Enter the number of the upper bound B: "))
random_list_11 = []

for _ in range(0, LIST_SIZE_11):
    random_list_11.append(random.randint(0, RANDOM_UPPER_BOUND_11))

set_b1 = set(random_list_11)
print(f"Set B: {set_b1}")

diff_set = set_a1.difference(set_b1)

if len(diff_set) == 0:
    print("Set A and B are the same.")
else:
    print(f"Set A has the {diff_set} different value/-s comparing with set B")

"""
Task 7
Напишите программу, которая удаляет пересечение 2-го набора
из 1-го набора.
"""

LIST_SIZE_12 = int(input("Enter the number of the set 1 size: "))
RANDOM_UPPER_BOUND_12 = int(input("Enter the number of the upper bound 1: "))
random_list_12 = []

for _ in range(0, LIST_SIZE_12):
    random_list_12.append(random.randint(0, RANDOM_UPPER_BOUND_12))

set_1 = set(random_list_12)
print(f"Set 1: {set_1}")

LIST_SIZE_13 = int(input("Enter the number of the set 2 size: "))
RANDOM_UPPER_BOUND_13 = int(input("Enter the number of the upper bound 2: "))
random_list_13 = []

for _ in range(0, LIST_SIZE_13):
    random_list_13.append(random.randint(0, RANDOM_UPPER_BOUND_13))

set_2 = set(random_list_13)
print(f"Set 2: {set_2}")

set_3 = set_1.intersection(set_2)
print(f"Intersection: {set_3}")

set_4 = set_1 - set_3

print(f"Set 1 except the intersection with set 2: {set_4}")

"""
Task 8 *
Реализовать логику Union для двух списков (list), проверить работу
алгоритма на set.union
"""

LIST_SIZE_14 = int(input("Enter the number of the list 1 size: "))
RANDOM_UPPER_BOUND_14 = int(input("Enter the number of the upper bound 1: "))
random_list_14 = []

for _ in range(0, LIST_SIZE_14):
    random_list_14.append(random.randint(0, RANDOM_UPPER_BOUND_14))

LIST_SIZE_15 = int(input("Enter the number of the list 2 size: "))
RANDOM_UPPER_BOUND_15 = int(input("Enter the number of the upper bound 2: "))
random_list_15 = []

for _ in range(0, LIST_SIZE_15):
    random_list_15.append(random.randint(0, RANDOM_UPPER_BOUND_15))

print(f"List 1: {random_list_14}")
print(f"List 2: {random_list_15}")

set_1a = set(random_list_14)
set_2a = set(random_list_15)

merged_lists = []

for i in random_list_14:
    if i not in merged_lists:
        merged_lists.append(i)

for j in random_list_15:
    if j not in merged_lists:
        merged_lists.append(j)

merged_lists.sort()

print(f"Merged lists: {merged_lists}")

# Test on set.union
test_set1 = set_1a.union(set_2a)
list_from_set = list(test_set1)

print(f"Merged lists based on sets: {list_from_set}")

"""
Task 9 *
Реализовать логику Difference для двух списков (list), проверить работу
алгоритма на set.difference
"""

LIST_SIZE_16 = int(input("Enter the number of the list 1 size: "))
RANDOM_UPPER_BOUND_16 = int(input("Enter the number of the upper bound 1: "))
random_list_16 = []

for _ in range(0, LIST_SIZE_16):
    random_list_16.append(random.randint(0, RANDOM_UPPER_BOUND_16))

LIST_SIZE_17 = int(input("Enter the number of the list 2 size: "))
RANDOM_UPPER_BOUND_17 = int(input("Enter the number of the upper bound 2: "))
random_list_17 = []

for _ in range(0, LIST_SIZE_17):
    random_list_17.append(random.randint(0, RANDOM_UPPER_BOUND_17))

print(f"List 1: {random_list_16}")
print(f"List 2: {random_list_17}")

set_1b = set(random_list_16)
set_2b = set(random_list_17)

diff_list1 = []

for i in random_list_16:
    if i not in random_list_17:
        if i not in diff_list1:
            diff_list1.append(i)

diff_list1.sort()

print(f"Difference between 1st and 2nd lists: {diff_list1}")

# Test on set.difference
test_set2 = set_1b.difference(set_2b)
list_from_sets1 = list(test_set2)
list_from_sets1.sort()

print(f"Difference between 1st and 2nd lists based on sets: {list_from_sets1}")
