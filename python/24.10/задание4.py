list = []
summ = 0
while True:
    a = int(input(""))
    
    if a == 7:
        break
    
    summ += a
    list.append(a)
    
    print("сумма =", summ,
          "\nмаксимум =", max(list),
          "\nминимум =", min(list))
    
print("Good bye!")