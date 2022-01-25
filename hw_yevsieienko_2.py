"""
Task 1
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
"""

n = int(input("Enter amount of km the car rides per day: "))
m = int(input("Enter the route length: "))

days = m // n
hours = ((m % n) / n) * 24
print(f"The car will reach the destination point in {days} days and {hours} hours.")

"""
Task 2
Пользователь вводит трехзначное число. Найдите сумму его цифр. (используйте %)
"""

user_number = int(input("Enter a three-digit number: "))

first_number = user_number // 100
second_number = user_number // 10 % 10
third_number = user_number % 10
numbers_sum = first_number + second_number + third_number
print(f"The sum of the numbers is {numbers_sum}.")

"""
Task 3
Найти максимальное число из трех. Числа вводится с клавиатуры
"""

number_1 = int(input("Enter the 1st number: "))
number_2 = int(input("Enter the 2nd number: "))
number_3 = int(input("Enter the 3rd number: "))

if number_1 > number_2 and number_1 > number_3:
    print("The first number is greater than the second and the third ones.")
elif number_2 > number_1 and number_2 > number_3:
    print("The second number is greater than the first and the third ones.")
else:
    print("The third number is greater than the first and the second ones.")

"""
Task 4
Определить високосный год или нет.Число вводится с клавиатуры
Год является високосным, если его номер кратен 4, но не кратен 100, или же если он кратен 400.
"""

user_year = int(input("Enter a year: "))

if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
    print(f"{user_year} is a leap year.")
else:
    print(f"{user_year} is NOT a leap year.")

"""
Task 5
Определить четное или нечетное число. Число вводится с клавиатуры
"""

user_input = int(input("Enter any number: "))

if user_input % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

"""
Task 6
Найти корни квадратного уравнения и вывести их на экран, если они есть. Если корней нет, то вывести сообщение об этом. 
Конкретное квадратное уравнение определяется коэффициентами a, b, c, которые вводит пользователь.
("a*(x**2)+b*x+c=0")
"""

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = b**2 - 4*a*c
print(f"Discriminant: {discriminant}")

if discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f"x1: {x1}")
    print(f"x2: {x2}")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"x: {x}")
else:
    print("There are NO roots.")

"""
Task 7
Дана следующая функция y=f(x):
y = 2x – 10, если x > 0
y = 0, если x = 0
y = 2 * |x| – 1, если x < 0
Найти значение функции по x, который вводиться с клавиатуры
"""

value_x = int(input("Enter value x: "))

if value_x > 0:
    value_y = 2 * value_x - 10
elif value_x == 0:
    value_y = 0
else:
    value_y = 2 * abs(value_x) - 1

print(f"Value y is equal to {value_y}")
