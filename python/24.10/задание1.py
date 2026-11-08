a = int(input("Введите начало диапозона: "))
b = int(input("Введите конец диапозона: "))
sumchet = 0
sum9 = 0
sumnech = 0
list9 = []
list2 = []
list3 = []

for i in range(a, b):
    if i % 9 == 0:
        sum9 += i
        list9.append(i)
        aver9 = sum(list9) / len(list9)
    elif i % 2 == 0:
        sumchet +=i
        list2.append(i)
        aver2 = sum(list2) / len(list2)
    else:
        sumnech += i
        list3.append(i)
        aver3 = sum(list3) / len(list3)

print("Кратные 9: сумма =", sum9, "среднее арифметическое =", aver9,
      "\nЧетные: сумма =", sumchet, "среднее арифметическое =", aver2,
      "\nНечетные: сумма =", sumnech, "среднее арифметическое =", aver3)