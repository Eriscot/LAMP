# -*- coding: cp1251 -*-
min = -1
min_i = -1
arr = []
n = input("Введите n => ")
for i in range(n):
    arr.append(input("Введите a[" + str(i) + "] => "))
    if arr[i] % 2 == 0:
        if min == -1 or min > arr[i]:
            min = arr[i]
            min_i = i
print(arr)
temp = arr[0]
arr[0] = arr[min_i]
arr[min_i] = temp
print(arr)

