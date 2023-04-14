import sys
input = sys.stdin.readline

n = int(input())

num = [0] * 10001  # 0 ~ 10000

for i in range(n):
    num[int(input())] += 1  # 입력받은 수의 인덱스에 1씩 더해줌

for i in range(10001):  # 0 ~ 10000
    if num[i] != 0:  # 0이 아닌 경우
        for j in range(num[i]):  # 해당 인덱스의 값만큼 반복
            print(i)  # 인덱스 출력
