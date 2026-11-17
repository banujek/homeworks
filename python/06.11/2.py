import random

list = []
nech = []
polog = []
otric = []
chet = []

a = random.randint(-20,0)
b = random.randint(1, 20)

for i in range(a, b):
    list.append(i)

while True:    
    for i in list:
        if i > 0:
            polog.append(i)
        elif i < 0:
            otric.append(i)
        
        if i % 2 == 0:
            chet.append(i)
        elif i % 2 != 0:
            nech.append(i)
        
    break

print(f"Спикок четных чисел - {chet}"
      f"\nСписок нечетных чисел - {nech}"
      f"\nСписок отрицательных чисел - {otric}"
      f"\nСписок положительных чисел - {polog}")