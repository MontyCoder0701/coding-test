import sys
input = sys.stdin.readline

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
s = input().strip()
li = []

for i in range(len(alpha)):
    li.append(s.find(alpha[i]))  # find()는 문자열에서 특정 문자의 위치를 반환한다. 없으면 -1을 반환한다.

for i in range(len(li)):
    print(li[i], end=' ')
