import random

"""
Вам дан код сортировки пузырьком, однако он работает неверно, там допущена ошибка.
Используя дебагер, найдите и исправьте ошибку.
Опишите в комментарии к коду, в чем была ошибка. Добавьте минимум 5 тестов для этого кода
"""

# def bubble_sort(l):
#     t = l.copy()
#     for n in range(0, len(t)):
#         for i in range(len(t) - n):
#             if t[i] > t[n]:
#                 t[i], t[n] = t[n], t[i]
#     return t
#
#
# nums = [4, 1, 6, 3, 2, 7, 8]
# sorted = bubble_sort(nums)
# print(sorted)


def bubble_sort(l):
    t = l.copy()
    for n in range(0, len(t)):
        for i in range(len(t) - n - 1):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]
    return t


# nums = [4, 1, 6, 3, 2, 7, 8, 0, 5]

# 5 tests
LIST_SIZE = int(input("Enter the number of the list size: "))
RANDOM_UPPER_BOUND = int(input("Enter the number of the upper bound: "))
my_list = [random.randint(0, RANDOM_UPPER_BOUND) for _ in range(LIST_SIZE)]
print(f"List: {my_list}")

sorted = bubble_sort(my_list)
print(f"Sorted list: {sorted}")


"""
Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся записи о номере заказа,
названии книги, количестве и стоимости одной книги, как представлено ниже, в таблице.
Напишите программу на Python, которая на вход получает список списков:
[
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения цены на товары и
количества. Стоимость товара должна быть увеличена на $10, если стоимость заказа меньше $100.
Программа должна использовать lambda и map.
"""

orders_list = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99]
]

print(f"Initial list: {orders_list}")

new_orders_list = list(map(lambda x: x if x[1] > 100 else (x[0], x[1] + 10),
                       map(lambda x: (x[0], x[2] * x[3]), orders_list)))

print(f"Total list: {new_orders_list}")

"""
Добавьте к исходному списку еще несколько товаров
[
[24387, " на русском", 2, 4.59],
[18762, "The C Programming Language (2nd Edition)", 12, 78.80],
[87236, "C Programming Absolute Beginner's Guide", 1, 23.55],
[58132, "Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14", 9,
42.89]
]
"""

add_orders_list = [
    [24387, " на русском", 2, 4.59],
    [18762, "The C Programming Language (2nd Edition)", 12, 78.80],
    [87236, "C Programming Absolute Beginner's Guide", 1, 23.55],
    [58132, "Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14", 9, 42.89]
]

print(f"Add-on to initial list: {add_orders_list}")

total_orders_list = [j for i in [orders_list, add_orders_list] for j in i]

print(f"Extended initial list: {total_orders_list}")

new_total_orders_list = list(map(lambda x: x if x[1] > 100 else (x[0], x[1] + 10),
                             map(lambda x: (x[0], x[2] * x[3]), total_orders_list)))

print(f"Extended total list: {new_total_orders_list}")

"""
Отсортируйте получившийся список по стоимости и выведите его на экран.
*Используйте lambda
"""

# sorted_orders_total = sorted(new_total_orders_list, lambda x: x[:-1])
#
# print(sorted_orders_total)

"""
Используя filter() оставьте только книги, количество которых больше 5ти. 
"""

filtered_list = list(filter(lambda x: x[-2] > 5, total_orders_list))

print(f"Filtered extended initial list: {filtered_list}")
