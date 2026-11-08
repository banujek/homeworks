#Задание 1
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона:"))

for i in range(a, b):
    if i % 16 == 0:
        print(i)