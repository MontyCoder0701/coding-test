import sys
input = sys.stdin.readline

stack = []

while True:
    line = input()

    if len(line) == 1:
        if line.strip() == ".":
            exit()

    for letter in line:
        if letter == '[' or letter == '(':
            stack.append(letter)
        if len(stack)>0 and stack[-1] == '[':
            if letter == ']':
                try:
                    stack.pop()
                except:
                    pass
        if len(stack)>0 and stack[-1] == '(':
            if letter == ')':
                try:
                    stack.pop()
                except:
                    pass

    if len(stack) == 0:
        print("yes")
    else:
        print("no")

    stack = []

