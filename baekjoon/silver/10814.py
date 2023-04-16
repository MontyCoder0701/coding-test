import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    # strip()은 양쪽 공백 제거, split()은 공백 기준으로 나눔
    li.append(input().strip().split())

li.sort(key=lambda x: int(x[0]))  # sort()는 기본적으로 오름차순 정렬, key는 정렬 기준

for i in li:
    print(i[0], i[1])
