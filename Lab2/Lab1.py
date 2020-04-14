# -*- coding: cp1251 -*-
# Replace the minimal even element with the first element and vice versa of a given array
min = -1
min_i = -1
arr = []
n = int(input("Enter n => "))
for i in range(n):
    arr.append(int(input("Enter a[" + str(i) + "] => ")))
    if arr[i] % 2 == 0:
        if min == -1 or min > arr[i]:
            min = arr[i]
            min_i = i
print(arr)
[arr[0], arr[min_i]] = [arr[min_i], arr[0]]
print(arr)

