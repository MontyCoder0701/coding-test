import sys
input = sys.stdin.readline

n = int(input())

# 다이나믹 프로그래밍 문제임 (3가지 경우가 제시되므로 나누어 해결)

dp = [0] * (n + 1)  # 최소 연산 횟수를 저장할 리스트

for i in range(2, n + 1):  # 1은 1로 만들 수 있으므로 2부터 시작
    dp[i] = dp[i - 1] + 1  # 1을 빼는 연산을 먼저 수행

    if i % 2 == 0:  # 2로 나누어 떨어지는 경우
        # 2로 나누는 연산을 수행한 횟수와 1을 빼는 연산을 수행한 횟수 중 최솟값을 저장
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:  # 3으로 나누어 떨어지는 경우
        # 3으로 나누는 연산을 수행한 횟수와 1을 빼는 연산을 수행한 횟수 중 최솟값을 저장
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
