import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

print(str(1-a) + " " + str(1-b) + " " + str(2 - c) +
      " " + str(2-d) + " " + str(2-e) + " " + str(8-f))
