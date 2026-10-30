"""
list1 = ["hop", 4, 86.3, "lk", 5]
list2 = ["op", 3]
list3 = ["op"]
list4 = list('kjh')
list5 = list(range(1, 9))


for i in range(1, 4):
    print(list1[0:2], list2[0], list3[0])
    print(list4)
    print(list5)

    
for i in list1:
    print(i)
    
o = len(list1)
print("len =", o)

for i in range(o):
    print(list1[i])
"""

#методы

list = ["lol", "kop", "fg", "ty", "tr", 4]
nlist = ["the", "chert"]
list.append("cool") #добавить элемент
list.extend(nlist)  #добавить список
list.insert(0, "best")  #добавить по индексу
list.remove("best")  #удалить элемент
list.pop(0)   #удаление по индексу
i = list.index("kop")    #поиск индекса
#list.clear()  #отчистка списка
print(list, "индекс = ", i)

nums = [4, 5, 7, 23, 6]
print(min(nums))
print(max(nums))
print(sum(nums))