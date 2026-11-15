import random
print("Введите 0 чтобы завершить программу")
p = 0
d = 0
f = 0
g = 0


while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    print(a, b)
    p += 1

    c = int(input("Введите произведение: "))

    if c == (b*a):
        print("Правильно")
        d += 1
    else:
        print("Неправильно")

    if c == 0:
        p -= 1
        break
g = d / p * 100

if g >= 90 and g <= 100:
    f += 5
elif g >= 80 and g < 90:
    f += 4
elif g >= 70 and g < 80:
    f += 3
else:
    f += 2
print("Ваша оценка:", f)
