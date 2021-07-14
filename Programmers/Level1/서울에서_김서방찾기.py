# 찾는 문자열이 배열의 몇 번째 인덱스인지 찾는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12919
# 그 동안 문자열은 + 연산으로 처리했는데 이 문제를 통해 format 함수로 처리하는 법을 배웠습니다.
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))