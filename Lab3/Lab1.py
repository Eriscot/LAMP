# -*- coding: cp1251 -*-
# Replace the minimal even element with the first element and vice versa of a given array
arr = []
n = int(input("Enter n => "))
for i in range(n):
    arr.append(int(input("Enter a[" + str(i) + "] => ")))
print(arr)


def calc(inputArr):
    min = -1
    min_i = -1
    for i in range(n):
        if inputArr[i] % 2 == 0:
            if min == -1 or min > inputArr[i]:
                min = inputArr[i]
                min_i = i
    [inputArr[0], inputArr[min_i]] = [inputArr[min_i], inputArr[0]]


calc(arr)

print(arr)
