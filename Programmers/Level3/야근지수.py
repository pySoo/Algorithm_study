# https://programmers.co.kr/learn/courses/30/lessons/12927
"""
문제
회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

제한사항
works는 길이 1 이상, 20,000 이하인 배열입니다.
works의 원소는 50000 이하인 자연수입니다.
n은 1,000,000 이하인 자연수입니다.

입출력
works	n	result
[4, 3, 3]	4	12
[2, 1, 2]	1	6
[1,1]	3	0
"""
# 효율성을 통과 못한 문제. n의 범위가 1<= n <=1,000,000 이므로 logN의 시간복잡도를 가진 힙의 연산을 수행해야한다.
# 값을 -부호로 변경하고 heapq를 이용하여 최대힙을 만든다.
# pop 연산으로 가장 작은값을(음수이므로 실제 값은 가장 크다) 찾아내서 1을 더한다.
import heapq


def solution(n, works):
    if n >= sum(works):
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    for _ in range(n):
        work = heapq.heappop(works) + 1
        heapq.heappush(works, work)

    return sum([i**2 for i in works])
