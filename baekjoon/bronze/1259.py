import sys
input = sys.stdin.readline

while True:  # 무한 반복
    n = input().rstrip()  # 입력받은 문자열의 오른쪽 공백 제거
    if n == '0':
        break
    if n == n[::-1]:  # 문자열을 뒤집어서 같은지 확인
        print('yes')
    else:
        print('no')
