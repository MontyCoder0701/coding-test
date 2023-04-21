import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]  # 1 ~ n
ans = []
index = 0

while arr:  # arr이 빌 때까지
    # index를 k만큼 이동. 이때, len(arr)로 나눈 나머지를 구해야 한바퀴를 돌고 다시 처음으로 돌아올 수 있음.
    index = (index + k - 1) % len(arr)
    ans.append(str(arr.pop(index)))  # pop한 값을 ans에 추가. str로 변환해야 추후 join이 가능.

print('<' + ', '.join(ans) + '>')
