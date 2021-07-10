# 문자열 활용 문제
# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    center = len(s) // 2
    if len(s) % 2 != 0:
        return s[center]
    else:
        return s[center-1:center+1]