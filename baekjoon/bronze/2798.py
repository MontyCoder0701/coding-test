import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

max = 0

for i in range(n):
    for j in range(i + 1, n):  # i + 1부터 시작하는 이유는 중복을 피하기 위함
        for k in range(j + 1, n):  # j + 1부터 시작하는 이유는 중복을 피하기 위함
            sum = nums[i] + nums[j] + nums[k]  # 세 수의 합
            if sum <= m and sum > max:  # 세 수의 합이 m보다 작거나 같고, max보다 크면 max에 저장
                max = sum

print(max)
