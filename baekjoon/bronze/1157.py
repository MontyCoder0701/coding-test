import sys
input = sys.stdin.readline

word = input().strip().upper()  # 입력받은 문자열을 모두 대문자로 바꾸고 양쪽 공백을 제거한다.
word_dict = {}  # 문자열의 각 문자를 key로, 문자의 개수를 value로 하는 딕셔너리를 생성한다.

for i in word:
    if i in word_dict:
        word_dict[i] += 1  # 문자가 이미 딕셔너리에 있으면 value를 1 증가시킨다.
    else:
        word_dict[i] = 1  # 문자가 딕셔너리에 없으면 key와 value를 추가한다.

max_value = max(word_dict.values())  # 딕셔너리의 value 중 최대값을 구한다.
max_key = []

for key, value in word_dict.items():  # 딕셔너리의 key와 value를 순회한다.
    if value == max_value:
        max_key.append(key)  # value가 최대값과 같으면 key를 max_key 리스트에 추가한다.

if len(max_key) > 1:
    print('?')
else:
    print(max_key[0])
