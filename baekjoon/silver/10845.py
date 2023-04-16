import sys
input = sys.stdin.readline

n = int(input())
queue = []

for i in range(n):
    li = input().strip().split()
    if len(li) > 1:
        if li[0] == "push":
            queue.append(li[1])
    else:
        if li[0] == "front":
            try:
                print(queue[0])
            except:
                print(-1)

        if li[0] == "back":
            try:
                print(queue[-1])
            except:
                print(-1)

        if li[0] == "pop":
            try:
                print(queue[0])
                queue.pop(0)
            except:
                print(-1)

        if li[0] == "size":
            print(len(queue))

        if li[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
