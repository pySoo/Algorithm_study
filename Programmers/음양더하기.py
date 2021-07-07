# 부호를 구분해서 더하는 문제
# zip() : iterable한 객체를 인자로 받아서 동일한 개수로 이루어진 데이터를 묶어 주는 역할
# https://programmers.co.kr/learn/courses/30/lessons/76501
def solution(absolutes, signs):
    answer = 0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer