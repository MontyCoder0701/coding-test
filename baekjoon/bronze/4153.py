import sys
input = sys.stdin.readline

li = list(map(int, input().split()))
li = sorted(li)

while not li[0] == li[1] == li[2] == 0:
    if pow(li[0], 2) + pow(li[1], 2) == pow(li[2], 2):
        print("right")
    else:
        print("wrong")
    li = list(map(int, input().split()))
    li = sorted(li)
