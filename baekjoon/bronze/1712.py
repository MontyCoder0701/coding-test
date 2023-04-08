import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if (c-b) == 0:
    print(-1)
else:
    x = a / (c-b)
    if x <= 0:
        print(-1)
    else:
        print(int(x+1))
