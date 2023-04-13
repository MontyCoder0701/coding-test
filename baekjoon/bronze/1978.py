import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))


def is_prime(n):  # use boolean
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


cnt = 0
for i in li:
    if is_prime(i):
        cnt += 1

print(cnt)
