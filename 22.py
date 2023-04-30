'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит в строку первый список затем на следующией строке второй список.
'''

numbers_1 = set([int(element) for element in input("Введите первый набор целых чисел: ").split()])
numbers_2 = set([int(element) for element in input("Введите второй набор целых чисел: ").split()])
common_numbers = numbers_1.intersection(numbers_2)
print(*sorted(common_numbers))