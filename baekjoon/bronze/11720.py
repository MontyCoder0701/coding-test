import sys
input = sys.stdin.readline

n = int(input())
base = 0
li = list(str(input().strip()))

for i in range(n):
    base += int(li[i])

print(base)
