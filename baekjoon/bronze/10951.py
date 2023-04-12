import sys
input = sys.stdin.readline

while True:  # EOFError가 발생할 때까지 반복
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
