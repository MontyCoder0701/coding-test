import sys
input = sys.stdin.readline

l, p = list(map(int, input().split()))
a, b, c, d, e = list(map(int, input().split()))

estimate = l * p

print(a - estimate, b - estimate, c - estimate, d - estimate, e - estimate)
