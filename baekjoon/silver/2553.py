import sys
input = sys.stdin.readline

a = int(input())


def factorial(a):
    fact = 1
    for i in range(1, a+1):  # 1부터 a까지
        fact *= i  # fact = fact * i
    return fact


fac_str = str(factorial(a))
fac_list = []

for i in range(len(fac_str)):
    fac_list.append(int(fac_str[i]))

fac_list = fac_list[::-1]

for i in range(len(fac_list)):
    if fac_list[i] == 0:
        continue
    else:
        print(fac_list[i])
        break
