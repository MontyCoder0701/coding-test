import sys


def powmod(a, b, m):  # a^b mod m
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result


def mr(n, a):  # Miller-Rabin primality test
    r = 0
    d = n-1
    while (d % 2 == 0):
        r += 1
        d = d // 2
    x = powmod(a, d, n)
    if x == 1 or x == n-1:
        return True
    for i in range(0, r-1):
        x = powmod(x, 2, n)
        if x == n-1:
            return True
    return False


def check_prime(k):  # 소수 판별
    check = 0
    if k <= 71:
        if k in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:  # 2~71까지의 소수
            return True
        else:
            return False
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if mr(k, i) == False:
                break
            else:
                check += 1
        if check == 12:
            return True
        else:
            return False


n = int(sys.stdin.readline())


def gcd(a, b):  # 최대공약수
    if b > a:  # a가 더 크게 만들기
        k = a
        a = b
        b = k
    while b != 0:  # 유클리드 호제법
        r = a % b
        a = b
        b = r
    return a


def g(x, n):  # f(x) = (x^2 + 1) mod n
    return ((x*x) + 1) % n


def pola(n, x):  # Pollard's rho algorithm
    p = x
    if check_prime(n):  # 소수인 경우
        return n
    else:
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:  # 2~71까지의 소수
            if n % i == 0:
                return i
        y = x
        d = 1
        while d == 1:  # d가 1이 아닐 때까지 반복
            x = g(x, n)
            y = g(g(y, n), n)
            d = gcd(abs(x-y), n)
        if d == n:  # d가 n과 같으면
            return pola(n, p+1)
        else:
            if check_prime(d):
                return d
            else:
                return pola(d, 2)


ans = []
while n != 1:
    k = pola(n, 2)  # n의 소인수 분해
    ans.append(int(k))  # 소인수를 ans에 추가
    n = n // k  # n을 소인수로 나눔
ans.sort()
for i in ans:
    print(i)
