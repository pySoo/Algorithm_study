# https://programmers.co.kr/learn/courses/30/lessons/43238
"""
문제
n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
심사관은 1명 이상 100,000명 이하입니다.

입출력
n	times	return
6	[7, 10]	28
"""
"""
알고리즘
1. 최소 시간 1분과 최대 시간인 최대 심사 시간 * 인원수를 left, right로 설정
2. left가 right 이하일 때 반복
3. 중간값과 심사 시간을 나눈 몫의 합이 n명 이상인지 확인
4-1. n명 이상이라면 시간을 더 줄일 수 있으므로 right = mid - 1
4-2. n명 미만이라면 시간을 줄일 수 없으므로 left = mid + 1
5. left 값이 최종 최소 시간
"""


def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2
        total = 0
        for t in times:
            total += mid // t
        if total >= n:
            right = mid
        else:
            left = mid + 1
    answer = left
    return answer
