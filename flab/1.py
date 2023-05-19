# https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3

# 문자열을 자를 단위를 1부터 문자열 길이의 절반까지 순서대로 증가시키면서 압축 문자열을 생성합니다.
# 생성한 압축 문자열의 길이를 기록하고, 가장 짧은 압축 문자열의 길이를 업데이트합니다.
# 자를 단위를 1씩 증가시키면서 위의 과정을 반복합니다.
# 가장 짧은 압축 문자열의 길이를 반환합니다.

def solution(s):
    answer = len(s) # 최대 길이
    for i in range(1, len(s)//2 + 1): # 1부터 문자열 길이의 절반까지 (문자열 길이의 절반보다 크게 자를 필요가 없음)
        temp = '' # 압축된 문자열
        cnt = 1 # 반복 횟수
        prev = s[:i] # 이전 문자열 
        for j in range(i, len(s), i): # i부터 문자열 길이까지 i만큼 증가 (i만큼씩 문자열을 자름)
            if prev == s[j:j+i]: # 이전 문자열과 같으면 반복 횟수 증가 
                cnt += 1 
            else: 
                if cnt == 1: # 반복 횟수가 1이면 생략
                    temp += prev 
                else:
                    temp += str(cnt) + prev # 반복 횟수 + 문자열
                cnt = 1  # 반복 횟수 초기화
                prev = s[j:j+i] # 이전 문자열 갱신 
        if cnt == 1: # 마지막 문자열 처리 
            temp += prev 
        else:
            temp += str(cnt) + prev 
        answer = min(answer, len(temp)) # 최소 길이 갱신
    return answer
