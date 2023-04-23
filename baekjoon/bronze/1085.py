import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min(min((h-y), (w-x)), min(x, y)))
