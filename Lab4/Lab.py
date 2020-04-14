# The program should delete all lowercase letters of Latin alphabet
# as well as count the amount of the vowels of Cyrillic alphabet
# and double all numbers
latin = "abcdefghijklmnopqrstuvwxyz"
russian = "аоуыяэюеиё"
russianCount = 0

str = input("Enter string =>")
resultStr = ""
for i in range(len(str)):
    if str[i] not in latin:
        if str[i] in russian:
            russianCount += 1
        resultStr += str[i]
        if str[i].isnumeric():
            resultStr += str[i]
print(str)
print("Russian vowels: ", russianCount)
print(resultStr)
