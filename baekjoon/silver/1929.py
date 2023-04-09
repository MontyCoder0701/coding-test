import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# 에라토스테네스의 체
prime = [True] * (n+1)  # n+1개의 True로 이루어진 리스트 생성
prime[0] = False  # 0은 소수가 아님
prime[1] = False  # 1은 소수가 아님

for i in range(2, int(n**0.5)+1):  # 2부터 n의 제곱근까지
    if prime[i]:  # i가 소수인 경우
        for j in range(i+i, n+1, i):  # i의 배수들을 False로 바꿈
            prime[j] = False

for i in range(m, n+1):  # m부터 n까지
    if prime[i]:  # i가 소수인 경우
        print(i)
