import sys
input = sys.stdin.readline

numbers = []

for i in range(int(input())):
    numbers.append(int(input()))

for i in sorted(numbers):
    print(i)
