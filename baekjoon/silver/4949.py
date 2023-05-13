import sys
input = sys.stdin.readline

stack = []

while True:
    string = input().rstrip() # rstrip() : 오른쪽 공백 제거
    if string == '.': # 종료 조건
        break # while문 종료
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)
                break
    if stack:
        print('no')
    else:
        print('yes')
    stack.clear() # 스택 초기화