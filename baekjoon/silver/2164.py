from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
li = []

for i in range(1, n+1):
    li.append(i)

q = deque(li)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
