import sys
input = sys.stdin.readline

sum = int(input())
n = int(input())
base = 0

for i in range(n):
    a, b = map(int, input().split())
    base += a*b

if sum == base:
    print("Yes")
else:
    print("No")
