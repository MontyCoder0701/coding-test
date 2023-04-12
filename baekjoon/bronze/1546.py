import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
maxer = max(li)
new_li = []

for item in li:
    new_li.append(item/maxer*100)

print(sum(new_li)/n)
