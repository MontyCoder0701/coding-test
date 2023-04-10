import sys
input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    a, b = map(int, input().split())
    li.append((a, b))

li = sorted(li)

for i in range(len(li)):
    print(str(li[i][0]) + " " + str(li[i][1]))
