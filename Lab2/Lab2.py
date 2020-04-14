# -*- coding: cp1251 -*-
# Replace the first negative element with the minimal 
# positive element and vice versa of a given array
neg_i = -1
last_pos = -1
pos_i = -1
arr = []
n = int(input("Enter n => "))
for i in range(n):
    arr.append(int(input("Enter a[" + str(i) + "] => ")))
    if neg_i == -1:
        if arr[i] < 0:
            neg_i = i
    if arr[i] > 0 and last_pos < arr[i]:
        last_pos = arr[i]
        pos_i = i
print(arr)
if neg_i != -1 and pos_i != -1:
    [arr[neg_i], arr[pos_i]] = [arr[pos_i], arr[neg_i]]
print(arr)

