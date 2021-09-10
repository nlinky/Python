#1) Создать 2 переменных типа String с разными значениями
first_name = 'Nadya'
last_name = 'Chervyakova'
#2) Создать 4 переменных типа Integer с разными значениями
age = 25
weight = 55
height = 163
imt = 20
#3) Создать 3 переменных типа Float с разными значениями
a = 45.45
b = 34.34
c = 78.87
#4) Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=.
# Pезультаты весвести в консоль.
print(age < imt)
print(weight > height)
print(age >= imt)
print(height <= weight)
print(age != imt)
print(age > weight)
print(height >= imt)
print(weight != imt)
print(height < age)
print(weight <= age)
print(imt >= height)
print(weight < imt)
print(weight != age)
print(imt >= weight)
print(age != height)
#5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=.
# Pезультаты весвести в консоль.
print(a < b)
print(a > b)
print(a != b)
print(b >= c)
print(b <= c)
print(b != c)
print(a <= c)
print(a > c)
print(a != c)
#6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not).
# Pезультаты весвести в консоль.
print(age < imt and weight > height)
print(age >= imt or height <= weight)
print(not age)
print(height >= imt and weight != imt)
print(height < age or weight <= age)
print(not imt)
print(weight != age and imt >= weight)
print(age != height or height >= imt)
print(not weight)
print(height >= imt and weight > height)
#7) Сделать скрипт используя функцию input().
#    1. Функция должна на вход принимать целое число.
#    2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"
chislo = int(input())
if chislo > 30:
    d = 'больше'
elif chislo < 30:
    d = 'меньше'
else:
     d = 'равно'

print("Вы вели число =", chislo, "которое", d, "30")

#8) Сделать скрипт используя функцию input().
#    1. Функция должна на вход принимать целое число.
#    2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#    3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"
import random
chislo_2 = int(input())
ran = random.randint(1, 100)
if chislo_2 > ran:
    d = 'больше'
elif chislo_2 < ran:
    d = 'меньше'
else:
    d = 'равно'

print("Вы вели число =", chislo_2, "которое", d, "сгенерированному числу")
print("Рандомное число =", ran)

#9) Сделать скрипт используя функцию input().
#    1. Функция должна на вход принимать целое число.
#    2. Внутри функции должно сгенерироваться рандомное 2 целых числа (import random)...(random.randint(1, 100))
#    3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
chislo_3 = int(input())
ran_1 = random.randint(1, 100)
ran_2 = random.randint(1, 100)
if chislo_3 > ran_1 and chislo_3 > ran_2:
    d = 'больше'
    c = 'больше'
elif chislo_3 > ran_1 and chislo_3 < ran_2:
    d = 'больше'
    c = 'меньше'
elif chislo_3 > ran_1 and chislo_3 == ran_2:
    d = 'больше'
    c = 'равно'
elif chislo_3 < ran_1 and chislo_3 < ran_2:
    d = 'меньше'
    c = 'меньше'
elif chislo_3 < ran_1 and chislo_3 > ran_2:
    d = 'меньше'
    c = 'больше'
elif chislo_3 < ran_1 and chislo_3 == ran_2:
    d = 'меньше'
    c = 'равно'
elif chislo_3 == ran_1 and chislo_3 > ran_2:
    d = 'равно'
    c = 'больше'
elif chislo_3 == ran_1 and chislo_3 < ran_2:
    d = 'равно'
    c = 'меньше'
else:
    d = 'равно'
    c = 'равно'

print("Вы вели число =", chislo_3, "которое", d, "и", c,"сгенерированному числу")
print("Рандомное число_1 =", ran_1)
print("Рандомное число_2 =", ran_2)











