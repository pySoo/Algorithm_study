# 문자열에 있는 p와 y의 개수가 같은지 판별하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12916
# 처음엔 counter을 사용해서 풀었으나 O(n)의 복잡도를 줄여보고자 다른 분의 해시를 이용한 O(1) 풀이를 참고하였습니다.
from collections import Counter
def solution(s):
    c = Counter(s.lower())
    return c['y'] == c['p']