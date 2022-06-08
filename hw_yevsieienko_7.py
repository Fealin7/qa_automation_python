import os
import random

"""
Напишите функцию для создания файла и записи в него случайных чисел, каждое число записывается в файл через пробел,
но не больше 10ти чисел в строку. Всего случайных чисел должно быть 1000
"""
FILE_NAME = 'homework'


def create_and_write_numbers_in_file(file_name):
    with open(f"{file_name}.txt", "w") as file:
        my_list = []
        for _ in range(100):
            random_list = random.sample(range(100), 10)
            my_string = " ".join(map(str, random_list)) + '\n'
            my_list.append(my_string)
        file.writelines(my_list)


# create_and_write_numbers_in_file(FILE_NAME)

"""
Напишите другую функцию, которая считывает первый файл и возводит каждое число в квадрат. 
Каждое полученное число должно быть дозаписано в исходный файл в таком же формате.
"""


def read_file_and_square_each_number(file_name):
    with open(f"{file_name}.txt", "r+") as file:
        my_list = file.readlines()
        for line in my_list:
            res = [int(i) ** 2 for i in line.split()]
            file.write(" ".join(map(str, res)) + '\n')


# read_file_and_square_each_number(FILE_NAME)

"""
Добавьте по 5 тестов для каждой функции
"""


# tests for create_and_write_numbers_in_file function
def test_create_and_write_numbers_in_file_if_file_is_created():
    create_and_write_numbers_in_file(FILE_NAME)
    file_exists = os.path.exists('homework.txt')
    assert file_exists is True


def test_create_and_write_numbers_in_file_if_file_not_empty():
    create_and_write_numbers_in_file(FILE_NAME)
    file_size = os.path.getsize('homework.txt')
    assert file_size != 0


def test_create_and_write_numbers_in_file_count_lines():
    create_and_write_numbers_in_file(FILE_NAME)
    actual = 0
    with open(f"{FILE_NAME}.txt", "r") as file:
        for _ in file:
            actual += 1
    expected = 100
    assert actual == expected


def test_create_and_write_numbers_in_file_count_numbers_in_file():
    create_and_write_numbers_in_file(FILE_NAME)
    actual = []
    with open(f"{FILE_NAME}.txt", "r") as file:
        for line in file:
            values = line.split(" ")
            for item in values:
                actual.append(item)
    expected = 1000
    assert len(actual) == expected


def test_create_and_write_numbers_in_file_count_numbers_in_line():
    create_and_write_numbers_in_file(FILE_NAME)
    actual = 0
    with open(f"{FILE_NAME}.txt", "r") as file:
        for line in file:
            actual = len(line.split(" "))
    expected = 10
    assert actual == expected


# tests for read_file_and_square_each_number function
def test_read_file_and_square_each_number_count_lines():
    read_file_and_square_each_number(FILE_NAME)
    actual = 0
    with open(f"{FILE_NAME}.txt", "r") as file:
        for _ in file:
            actual += 1
    expected = 200
    assert actual == expected


def test_read_file_and_square_each_number_count_numbers_in_file():
    # read_file_and_square_each_number(FILE_NAME)
    actual = []
    with open(f"{FILE_NAME}.txt", "r") as file:
        for line in file:
            values = line.split(" ")
            for item in values:
                actual.append(item)
    expected = 2000
    assert len(actual) == expected


def test_read_file_and_square_each_number_count_numbers_in_line():
    # read_file_and_square_each_number(FILE_NAME)
    actual = 0
    with open(f"{FILE_NAME}.txt", "r") as file:
        for line in file:
            actual = len(line.split(" "))
    expected = 10
    assert actual == expected

