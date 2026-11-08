#Задание 2
a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона:"))
list= []
count = 0
for i in range(a, b):
    print(i, end=" ")
    list.append(i)

list.sort(reverse=True)
print("\n",list)
    
for i in range(a, b):
    if i % 7 == 0:
        print(i, end=" ")
    
    if i % 5 == 0:
        count += 1
print("\n",count)