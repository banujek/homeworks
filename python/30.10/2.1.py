a = input("Введите число: ")
summ = 0
count = 0
count_zero = 0
middle = 0

for i in (a):
    summ += int(i)
    count += 1
    if i == "0":
        count_zero += 1
middle = summ / count

print("Сумма цифр =", summ, "\nКол-во цифр =", count, "\nКол-во нулей =", count_zero, "\nСреднее арифметическое =", middle)
