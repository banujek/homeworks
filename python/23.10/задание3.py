#Задание 3
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона:"))

for i in range(a, b):
    if i % 3 ==0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)