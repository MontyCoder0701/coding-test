import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

mult = str(a*b*c)
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
index = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

for letter in mult:
    for i in range(len(num)):
        if letter == num[i]:
            index[i] += 1

for item in index:
    print(item)
