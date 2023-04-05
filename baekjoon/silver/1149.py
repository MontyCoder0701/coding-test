import sys
input = sys.stdin.readline

n = int(input())
cost = []  # 각 집을 칠하는 비용을 저장할 리스트

for i in range(n):
    cost.append(list(map(int, input().split())))  # 각 집을 칠하는 비용을 저장

dp = [[0]*3 for _ in range(n)]  # 각 집을 칠하는 비용의 최솟값을 저장할 리스트
dp[0] = cost[0]  # 첫 번째 집을 칠하는 비용을 저장

for i in range(1, n):  # 두 번째 집부터 마지막 집까지
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]  # 빨간색을 칠하는 경우
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]  # 초록색을 칠하는 경우
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]  # 파란색을 칠하는 경우

print(min(dp[n-1]))  # 마지막 집을 칠하는 비용의 최솟값 출력
