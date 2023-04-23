import sys
input = sys.stdin.readline

n = int(input())
have = list(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))


# have를 dict로 만들어서 key는 숫자, value는 개수로 저장.
have_dict = {}
for i in have:
    if i in have_dict:  # 이미 have_dict에 있는 숫자면 value를 1 증가.
        have_dict[i] += 1
    else:
        have_dict[i] = 1  # 처음 나오는 숫자면 value를 1로 저장.

print(have_dict)

# want를 순회하면서 have_dict에 있는지 확인. 있으면 value를 출력하고, 없으면 0을 출력.
for i in want:
    if i in have_dict:
        print(have_dict[i], end=' ')
    else:
        print(0, end=' ')
