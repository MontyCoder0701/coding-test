import sys
input = sys.stdin.readline
# 백줌 문제의 경우 input() 대신 sys.stdin.readline()을 사용해야 시간초과가 나지 않는다.

numbers = []

for i in range(int(input())):
    numbers.append(int(input()))

for i in sorted(numbers):
    print(i)  # 한 줄에 하나씩 출력
