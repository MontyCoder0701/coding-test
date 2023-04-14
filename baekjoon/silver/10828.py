import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    li = input().strip().split()
    if len(li) > 1:
        if li[0] == "push":
            stack.append(li[1])
    else:
        if li[0] == "pop":
            try:
                print(stack[-1])
                stack.pop()
            except:
                print(-1)
        if li[0] == "top":
            try:
                print(stack[-1])
            except:
                print(-1)
        if li[0] == "size":
            print(len(stack))
        if li[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
