import sys
input = sys.stdin.readline

li = []

for i in range(10):
    li.append(int(input()) % 42)

liset = set(li)

print(len(liset))
