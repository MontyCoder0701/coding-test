import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))  # (값, 인덱스) 튜플로 저장

# 둘을 비교하기 위해 정렬
sorted_arr = sorted(arr)
answer = []

for i in range(n):
    answer.append(sorted_arr[i][1] - arr[i][1])  # 정렬된 배열의 인덱스 - 원래 배열의 인덱스

print(max(answer) + 1)  # 인덱스는 0부터 시작하므로 +1
