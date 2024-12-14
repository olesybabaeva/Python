#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

list1 = [3, 4, 4, 6, 14, 14, 25, 26, 26]
for item in list1:
    if list1.count(item) < 2:
        for i in range(list1.count(item)):
          list1.remove(item)
list2 = set(list1)

print(list2)
