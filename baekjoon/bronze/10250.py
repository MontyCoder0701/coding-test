import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:  # n이 h의 배수일 때
        print(h * 100 + n // h)  # 100의 자리에 h를 넣고, 1의 자리에 n//h를 넣는다.
    else:
        # 100의 자리에 n%h를 넣고, 1의 자리에 n//h+1을 넣는다.
        print((n % h) * 100 + n // h + 1)
