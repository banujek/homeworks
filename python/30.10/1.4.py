a = int(input("Введите длину: "))
b = int(input("Введите высоту: "))
i, j = 0, 0

while i < b:
    if i == 0 or i == b - 1:
        print("*" * a)
    else:
        print("*" + " " * (a - 2) + "*")
    i += 1
