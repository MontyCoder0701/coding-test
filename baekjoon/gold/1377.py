import sys
N = int(sys.stdin.readline())
A = [0] + [int(sys.stdin.readline())
           for _ in range(N)]  # 0 is added for convenience

changed = False
for i in range(1, N+2):  # N+2 is the last index to be compared
    changed = False
    for j in range(1, N-i+1):  # N-i+1 is the last index to be compared
        if A[j] > A[j+1]:
            changed = True
            A[j], A[j+1] = A[j+1], A[j]
    if not changed:  # if no change is made, the list is sorted
        print(i)
        break
