import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
else:
    i = 1  # i번째 방
    while n > 1:  # 1번째 방은 1개
        n -= 6*i  # 2번째 방부터 6개씩 늘어남
        i += 1  # 2번째 방부터 1씩 증가
    print(i)
