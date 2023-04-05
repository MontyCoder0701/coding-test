import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())

a %= b  # a를 b로 나눈 나머지
for i in range(n-1):  # n-1번 반복
    a *= 10  # a에 10을 곱함
    a %= b  # a를 b로 나눈 나머지

print((a*10)//b)  # a에 10을 곱한 후 b로 나눈 몫
