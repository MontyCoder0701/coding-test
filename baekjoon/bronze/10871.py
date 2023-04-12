import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))

lili = []

for item in li:
    if item < m:
        print(str(item) + " ", end="")
