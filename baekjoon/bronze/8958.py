import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    test = input()  # OX퀴즈의 결과를 입력받는다.
    score = 0  # 점수를 저장할 변수
    total = 0  # 총 점수를 저장할 변수
    for j in range(len(test)):
        if test[j] == 'O':
            score += 1  # 점수를 1점씩 더해준다.
            total += score  # 총 점수에 점수를 더해준다.
        else:
            score = 0  # 점수를 0으로 초기화한다.
    print(total)
