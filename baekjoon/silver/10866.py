import sys
input = sys.stdin.readline

n = int(input())
dequeue = []

for i in range(n):
    li = input().strip().split()
    if len(li) > 1:
        if li[0] == "push_front":
            dequeue.insert(0, li[1])
        if li[0] == "push_back":
            dequeue.append(li[1])
    else:
        if li[0] == "front":
            try:
                print(dequeue[0])
            except:
                print(-1)

        if li[0] == "back":
            try:
                print(dequeue[-1])
            except:
                print(-1)

        if li[0] == "pop_front":
            try:
                print(dequeue[0])
                dequeue.pop(0)
            except:
                print(-1)

        if li[0] == "pop_back":
            try:
                print(dequeue[-1])
                dequeue.pop()
            except:
                print(-1)

        if li[0] == "size":
            print(len(dequeue))

        if li[0] == "empty":
            if len(dequeue) == 0:
                print(1)
            else:
                print(0)

        if li[0] == "pop":
            try:
                print(dequeue[0])
                dequeue.pop(0)
            except:
                print(-1)

        if li[0] == "push":
            dequeue.append(li[1])
