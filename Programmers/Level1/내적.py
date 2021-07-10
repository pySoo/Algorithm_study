# 각 리스트의 인덱스끼리 곱하고 총합을 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])