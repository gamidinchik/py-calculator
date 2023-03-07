# starting the code
import math

num1 = input("Введите первое число ")
num2 = input("Введите второе число ")
print(num1)
print(num2)


def divide(x, y):
    return math.trunc(x / y)


def multiply(x, y):
    return math.trunc(x * y)


def add(x, y):
    return math.trunc(x + y)


def subtract(x, y):
    return math.trunc(x - y)


print("{} + {} =".format(num1, num2), add(int(num1), int(num2)))
print("{} / {} =".format(num1, num2), divide(int(num1), int(num2)))
print("{} * {} =".format(num1, num2), multiply(int(num1), int(num2)))
print("{} - {} =".format(num1, num2), subtract(int(num1), int(num2)))
