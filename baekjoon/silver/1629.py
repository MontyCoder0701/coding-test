import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())


def power(a, b):
    if b == 1:  # b가 1이면 a를 c로 나눈 나머지를 반환
        return a % c
    else:
        temp = power(a, b // 2)  # b가 짝수면 a를 b//2번 곱한 값의 제곱을 c로 나눈 나머지를 반환
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c  # b가 홀수면 a를 b//2번 곱한 값의 제곱에 a를 곱한 값의 c로 나눈 나머지를 반환


print(power(a, b))
