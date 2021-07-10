# 두 정수 사이의 연속된 수들의 합을 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12912
# 연속된 수를 구하는 문제에서 range를 활용해야겠습니다.
def solution(a, b):
    if a < b :
        return sum(list(range(a, b+1)))
    else:
        return sum(list(range(b, a+1)))