# -*- coding: cp1251 -*-
# Replace the first negative element with the minimal 
# positive element and vice versa of a given array
arr = []
n = int(input("Enter n => "))
for i in range(n):
    arr.append(int(input("Enter a[" + str(i) + "] => ")))


def calc(inputArr):
    neg_i = -1
    last_pos = -1
    pos_i = -1
    for i in range(n):
        if neg_i == -1:
            if inputArr[i] < 0:
                neg_i = i
        if inputArr[i] > 0 and last_pos < inputArr[i]:
            last_pos = inputArr[i]
            pos_i = i
    if neg_i != -1 and pos_i != -1:
        [inputArr[neg_i], inputArr[pos_i]] = [inputArr[pos_i], inputArr[neg_i]]


calc(arr)

print(arr)
