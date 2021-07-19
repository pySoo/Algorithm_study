# 정수 -> 문자열 -> 리스트 -> 정렬 -> 정수로 변환하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12933
# sort 함수는 리스트만 가능하며 리스트를 한 문자로 만들기 위해서는 join을 사용합니다.
def solution(n):
    l = list(str(n))
    l.sort(reverse=True)
    return int(''.join(l))