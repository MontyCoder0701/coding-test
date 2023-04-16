import sys
input = sys.stdin.readline

n, k = map(int, input().split())
base = 1  # 0으로 초기화하면 0이 출력됨

for i in range(n, n-k, -1):  # n부터 n-k까지 -1씩 감소
    base *= i  # base = base * i

for i in range(1, k+1):  # 1부터 k까지 1씩 증가
    base //= i  # base = base // i

print(base)
