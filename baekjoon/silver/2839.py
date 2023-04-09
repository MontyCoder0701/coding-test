import sys
input = sys.stdin.readline

n = int(input())

# 다이나믹 프로그래밍 사용 (Bottom-up)


def sugar(n):  # nkg의 설탕을 배달하는 봉지의 최소 개수를 반환하는 함수
    for i in range(n//5, -1, -1):  # 5kg 봉지의 최대 개수부터 0까지 (거꾸로)
        for j in range(n//3, -1, -1):  # 3kg 봉지의 최대 개수부터 0까지 (거꾸로)
            if 5*i + 3*j == n:  # 5kg 봉지 i개와 3kg 봉지 j개를 사용했을 때 nkg이 되는 경우
                return i+j  # 봉지의 최소 개수
    return -1


print(sugar(n))
