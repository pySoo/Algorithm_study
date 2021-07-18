# 행렬의 덧셈 결과를 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12950
# zip을 활용하면 한 줄로도 풀 수 있었습니다.
# for a, b in zip(arr1, arr2) = [1, 4] [2, 3]
# for c, d in zip(a, b) = 1,2 / 4, 3
def solution(arr1, arr2):
    return [[c + d for c, d in zip(a, b)] for a , b in zip(arr1, arr2)]