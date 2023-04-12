import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if m < 45:
    if n == 0:
        n = n + 24
    n = n-1
    m = m + 60

print(n, m-45)
