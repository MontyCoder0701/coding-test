import sys
input = sys.stdin.readline

li = list(map(int, input().split()))  # list로 받고 int로 바꿔준다.

if li == sorted(li):
    print("ascending")
elif li == sorted(li, reverse=True):
    print("descending")
else:
    print("mixed")
