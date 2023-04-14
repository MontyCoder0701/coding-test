from math import gcd, lcm
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))
