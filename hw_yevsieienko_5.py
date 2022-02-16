import random

"""
Task 1
Напишите функцию calculations () так, чтобы она могла принимать две переменные и вычислять их сложение и вычитание.
А также он должен возвращать как сложение, так и вычитание за один вызов возврата.
"""
first_number = int(input("Enter your number 1: "))
second_number = int(input("Enter your number 2: "))


def calculations():
    sum_numbers = first_number + second_number
    subtr_numbers = first_number - second_number
    return sum_numbers, subtr_numbers


print(calculations())

"""
Task 2
Напишите функцию Python для суммирования всех чисел в списке.
"""
LIST_SIZE = int(input("Enter the number of the list size: "))
RANDOM_UPPER_BOUND = int(input("Enter the number of the upper bound: "))
my_list = []

for _ in range(0, LIST_SIZE):
    my_list.append(random.randint(0, RANDOM_UPPER_BOUND))

print(f"List: {my_list}")


def listSum():
    sum_list_numbers = 0
    for i in my_list:
        sum_list_numbers += i
    return sum_list_numbers


print(listSum())

"""
Task 3
Напишите функцию func () так, чтобы она могла принимать аргументы переменной длины 
и выводить все значения аргументов с индексом аргумента.
"""


def func(*args):
    for index in range(len(args)):
        print(f"Value: {args[index]}, Index: {index}")


func(1, 2, 5, 10, 15)

"""
Task 4
Создайте функцию showEmployee () таким образом, чтобы она принимала имя сотрудника и его зарплату и отображала и то, 
и другое. Если в вызове функции отсутствует зарплата, присвойте зарплате значение по умолчанию 9000.
"""


def showEmployee(name, salary=9000):
    return name, salary


print("Name of the employee and their salary")
print(showEmployee(name="Jack Smith"))

"""
Task 5
Дано натуральное число N. Вычислите сумму его цифр. Напишите рекурсивную функцию
"""

n = int(input("Enter your number: "))


def sumDigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumDigits(n // 10)


print(sumDigits(n))

"""
Task 6
Напишите рекурсивную функцию для вычисления числа Фибоначи
"""


fib = int(input("Enter fibonacci number: "))


def fibonacci(fib):
    if fib == 0:
        return 0
    elif fib in (1, 2):
        return 1
    else:
        return fibonacci(fib - 1) + fibonacci(fib - 2)


print(fibonacci(fib))

"""
Task 7
Напишите функцию для умножения всех чисел в списке. Рекурсивно
"""
LIST_SIZE_0 = int(input("Enter the number of the list size: "))
RANDOM_UPPER_BOUND_0 = int(input("Enter the number of the upper bound: "))
my_list_0 = []

for _ in range(0, LIST_SIZE_0):
    my_list_0.append(random.randint(0, RANDOM_UPPER_BOUND_0))

print(f"List: {my_list_0}")


def multiply(my_list_0):
    if len(my_list_0) == 1:
        return my_list_0[0]
    else:
        return my_list_0[0] * multiply(my_list_0[1:])


print(multiply(my_list_0))

"""
Task 8
Дано натуральное число N. 
Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае. 8 - YES, 3 - NO
"""
my_num = int(input("Enter your number to check if it's the exact power of 2: "))


def myFunc(my_num):
    if my_num % 1:
        return "NO"
    if my_num > 2:
        return myFunc(my_num / 2)
    if my_num:
        return "YES"


print(myFunc(my_num))

"""
Task 9
Создайте inner функцию для вычисления сложения следующим образом:
1. Создайте внешнюю функцию, которая будет принимать два параметра, a и b
2. Создайте внутреннюю функцию внутри внешней функции, которая будет вычислять сложение a и b
3. Наконец, внешняя функция добавит 5 и вернет ее.
"""


def outer():
    a = 5
    b = 10

    def inner():
        nonlocal a, b
        return a + b

    return (inner()) + 5


print(outer())


# def outer1(a, b):
#     def inner1():
#         return a + b
#     return (inner1()) + 5
#
#
# print(outer1(1, 1))
