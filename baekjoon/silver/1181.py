import sys
input = sys.stdin.readline

n = int(input())

words = set()  # 중복 제거

for _ in range(n):  # _는 반복문에서 사용되는 변수이지만, 특별한 용도로 사용되지 않는다는 것을 의미
    words.add(input().strip())  # strip()은 문자열 양쪽의 공백을 제거하는 함수

words = list(words)  # set은 인덱싱이 불가능하므로 list로 변환
words.sort(key=lambda x: (len(x), x))  # 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬

for word in words:  # 정렬된 단어들을 출력
    print(word)
