import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = []
for i in range(n):
    # rstrip()으로 개행문자 제거. 아니면 check함수에서 64-cnt에서 1을 빼야함.
    li.append(list(input().rstrip()))


def check(x, y):  # x, y는 체스판의 왼쪽 위 모서리 좌표
    cnt = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j) % 2 == 0:  # 짝수번째 행, 홀수번째 행
                if li[i][j] != 'W':
                    cnt += 1
            else:
                if li[i][j] != 'B':
                    cnt += 1
    return min(cnt, 64-cnt)  # 64-cnt는 체스판을 다 바꾸는 경우


ans = 64  # 체스판을 다 바꾸는 경우
for i in range(n-7):
    for j in range(m-7):
        ans = min(ans, check(i, j))  # 체스판을 다 바꾸는 경우와 비교

print(ans)
