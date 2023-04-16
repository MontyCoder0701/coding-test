import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

if (v-a) % (a-b) == 0:  # 나누어 떨어지면
    print((v-a) // (a-b) + 1)
else:
    print((v-a) // (a-b) + 2)
