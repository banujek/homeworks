import random

list = []
list1 = []

sumot = 0
sumch = 0
sumnech = 0
pro3 = 1
prois = 1
prois1 = 1

a = random.randint(-20,0)
b = random.randint(1, 20)

for i in range(a, b):
    list.append(i)

while True:    
    for i in list:
        if i < 0:
            sumot += i
        elif i > 0:
            list1.append(i)
        
        if i % 2 == 0:
            sumch += i
        elif i % 2 !=0:
            sumnech += i
        elif i % 3 == 0:
            pro3 *= i
        
        if i == 0:
            list.remove(0)
    
    list.sort(reverse=False)
    er = list.pop(0)
    we = list.pop()
    
    for i in list:
        prois *= i
        
    list1.sort(reverse=False)
    tr = list1.pop(0)
    df = list1.pop()
        
    for i in list1:
            prois1 *= i
        
    break
    
print(f"Сумма отрицательных чисел = {sumot}" 
      f"\nСумма четных чисел = {sumch}"
      f"\nСумма нечетных чисел = {sumnech}"
      f"\nПроизведение элементов кратных 3 = {pro3}"
      f"\nПроизведение элементов между минимальным и максимальным = {prois}"
      f"\nСумма элементов,находящихся между первым и последним положительными элементами = {prois1}")