import random

"""
Task 2
Напишите программу Python, которая принимает слово от пользователя и переворачивает его
Пример: input - Hello Worlds output - sdlroW olleH
"""

user_words = input("Enter your word/sentence: ")

for i in range(len(user_words) - 1, -1, -1):
    print(user_words[i], end="")
print("")

"""
Task 3
Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

height = int(input("Enter any number starting with 2: "))

for i in range(height):
    for _ in range(i):
        print("* ", end="")
    print("")
for i in range(height, 0, -1):
    for _ in range(i):
        print("* ", end="")
    print("")


"""
Task 4
Даны два целых числа A и В. 
Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания если A > B
"""

number_a = int(input("Enter number a: "))
number_b = int(input("Enter number b: "))

if number_a < number_b:
    for num in range(number_a, number_b + 1):
        print(num, end=" ")
else:
    for num in range(number_a, number_b - 1, -1):
        print(num, end=" ")


"""
Task 5
Даны два целых числа A и B (при этом A < B). Выведите все числа от A до B включительно.
"""

a = int(input("Enter number a: "))
b = int(input("Enter number b > a: "))

if a < b:
    for item in range(a, b + 1):
        print(item, end=" ")
else:
    print("Your input doesn't match the condition.")
print("")

"""
Task 6
Напишите программу, которая удаляет дубликаты элементов из списка.
"""

LIST_SIZE = 20
RANDOM_UPPER_BOUND = 10
my_list = []

for _ in range(0, LIST_SIZE):
    my_list.append(random.randint(0, RANDOM_UPPER_BOUND))
print(my_list)

new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

"""
Task 7
Напишите программу, которая копирует список
"""

LIST_SIZE_0 = 10
RANDOM_UPPER_BOUND_0 = 10
my_random_list = []

for _ in range(0, LIST_SIZE_0):
    my_random_list.append(random.randint(0, RANDOM_UPPER_BOUND_0))
print(f"List: {my_random_list}")

copy_list = []

for i in my_random_list:
    copy_list.append(i)

print(f"Copied list, option 1: {copy_list}")

copy_list_alt = my_random_list
copy_list_alt1 = list(my_random_list)

print(f"Copied list, option 2: {copy_list_alt}")
print(f"Copied list, option 3: {copy_list_alt1}")

"""
Task 8
Напишите программу, которая находит разницу между двумя списками и сохраняет ее в новый список. 
Вывести результат на экран. 
"""

LIST_SIZE_1 = 10
RANDOM_UPPER_BOUND_1 = 10
my_list_1 = []

LIST_SIZE_2 = 5
RANDOM_UPPER_BOUND_2 = 10

my_list_2 = []

for _ in range(0, LIST_SIZE_1):
    my_list_1.append(random.randint(0, RANDOM_UPPER_BOUND_1))
print(my_list_1)

for _ in range(0, LIST_SIZE_2):
    my_list_2.append(random.randint(0, RANDOM_UPPER_BOUND_2))
print(my_list_2)

unique_list = []

for i in my_list_1:
    if i not in my_list_2:
        if i not in unique_list:
            unique_list.append(i)

for j in my_list_2:
    if j not in my_list_1:
        if j not in unique_list:
            unique_list.append(j)

print(f"List with different values from two lists: {unique_list}")

"""
Task 9
Напишите программу для объединения следующих словарей для создания нового
Исходные словари :

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Результат : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = dict()

for i in dic1, dic2, dic3:
    dic4.update(i)

print(dic4)

"""
Task 10
Напишите программу, которая выводит словарь, в котором ключи представляют собой числа от 1 до 15 (оба включены), 
а значения представляют собой квадраты ключей. Генерация ключей и значений должна быть выполнена через цикл. 
"""

my_dict = dict()

for i in range(1, 16):
    my_dict[i] = i**2

print(my_dict)
