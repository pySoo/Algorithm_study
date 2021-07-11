# 내림차순으로 배치할 때 소문자는 대문자보다 우선시 됩니다. join -> 리스트를 문자열로 합쳐줍니다.
# https://programmers.co.kr/learn/courses/30/lessons/12917
def solution(s):
    return ''.join(sorted(s,reverse=True))