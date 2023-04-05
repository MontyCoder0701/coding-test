import sys
input = sys.stdin.readline

n = int(input())

triangle = []  # 삼각형의 각 줄을 저장할 리스트

for i in range(n):
    triangle.append(list(map(int, input().split())))  # 삼각형의 각 줄을 저장

# 나눠서 생각해봐야 하기때문에 dp 문제임.
dp = [[0]*n for _ in range(n)]  # 삼각형의 각 줄에서 각 위치까지의 최대 경로 합을 저장할 리스트

dp[0][0] = triangle[0][0]  # 첫 번째 줄의 첫 번째 위치의 값 저장

for i in range(1, n):  # 두 번째 줄부터 마지막 줄까지
    dp[i][0] = dp[i-1][0] + triangle[i][0]  # 첫 번째 위치의 값 저장
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]  # 마지막 위치의 값 저장

for i in range(2, n):  # 세 번째 줄부터 마지막 줄까지
    for j in range(1, i):  # 두 번째 위치부터 마지막에서 두 번째 위치까지
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + \
            triangle[i][j]  # 현재 위치의 값 저장

print(max(dp[n-1]))  # 마지막 줄에서 최대 경로 합 출력
