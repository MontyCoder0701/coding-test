import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    li = list(input().rstrip())
    cnt = 0
    for j in li:
        if j == '(':
            cnt += 1
        elif j == ')':
            cnt -= 1
        if cnt < 0:  # if cnt < 0, it means that ')' is more than '('
            print('NO')
            break
    if cnt > 0:  # if cnt > 0, it means that '(' is more than ')'
        print('NO')
    elif cnt == 0:
        print('YES')
