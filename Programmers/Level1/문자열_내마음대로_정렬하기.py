# n번째 문자 기준 오름차순 정렬하고 같다면 전체 문자들을 사전순으로 정렬하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    # sorted에서 lambda 우측에 (,) 두 개의 인자를 주어 x[n]이 같다면 x 순으로 정렬함을 뜻함
    return sorted(strings, key = lambda x : (x[n], x))