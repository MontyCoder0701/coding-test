import sys
input = sys.stdin.readline

n = int(input())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)  # 재귀함수를 이용한 팩토리얼 구하기


print(factorial(n))
