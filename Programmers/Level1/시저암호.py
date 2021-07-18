# 알파벳 문자열을 n만큼 민 암호문을 만드는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12926
# char() 아스키 값을 입력 받아 문자로 변환하는 함수
# ord() 문자를 아스키 값으로 변환하는 함수 
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        # a에서부터 시작하기 때문에 마지막에 ord('a')를 해주어야합니다.
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s)