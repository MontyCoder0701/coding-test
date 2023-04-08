import sys
input = sys.stdin.readline

d, h, w = map(int, input().split())  # d: diagonal, h: height, w: width

# ratio: ratio of diagonal to height and width
ratio = d / (h ** 2 + w ** 2) ** 0.5

print(int(h * ratio), int(w * ratio))
