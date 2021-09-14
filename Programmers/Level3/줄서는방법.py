# https://programmers.co.kr/learn/courses/30/lessons/12936
"""
문제
n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

제한사항
n은 20이하의 자연수 입니다.
k는 n! 이하의 자연수 입니다.

입출력
n	k	result
3	5	[3,1,2]
"""
import math


def solution(n, k):
    answer = []
    lst = [x for x in range(1, n+1)]

    while lst:
        # 첫 번째 문자는 고정하고 나머지 문자들의 경우의 수를 구한다.
        # 맨 앞이 1,2,3일 때 뒤에 올 수 있는 2자리의 경우의 수는 2! = 2
        temp = math.factorial(n-1)
        # divmod(5,2)에서 q=2 r=1 나머지가 있으므로 2번째 인덱스
        q, r = divmod(k, temp)
        q = q-1 if r == 0 else q

        # [1,2,3]에서 3을 뽑아서 정답에 추가
        answer.append(lst.pop(q))

        # 3으로 시작하는 것 알았으니 n 감소
        n -= 1
        # 나머지의 순서에 배치될 숫자를 재탐색
        k = r

    return answer
