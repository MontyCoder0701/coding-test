import sys
input = sys.stdin.readline

n, m = map(str, input().split())

n = int(n[::-1])
m = int(m[::-1])

print(max(n, m))
