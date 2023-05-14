import sys
input = sys.stdin.readline

n = int(input())
cnt = 0 # 666이 들어간 수의 개수
num = 666 # 666부터 시작

while True:
    if '666' in str(num):  # num에 666이 들어가면 cnt를 1 증가시키고, cnt가 n과 같아지면 num을 출력하고 break
        cnt += 1
    if cnt == n:
        print(num) 
        break
    num += 1
