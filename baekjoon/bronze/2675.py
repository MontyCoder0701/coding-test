import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    r, s = input().split()
    r = int(r)

    for j in range(len(s)):
        print(s[j] * r, end='')  # end=''로 줄바꿈을 없애준다.
    print()  # 한 줄을 다 출력한 후 줄바꿈을 해준다.
