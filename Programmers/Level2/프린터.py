# 스택, 큐를 활용하는 우선순위 고려 문제
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque
def solution(priorities, location):
    answer = 0
    # 값, 인덱스 순서
    q = deque([(v,i) for i,v in enumerate(priorities)])
    while len(q):
        item = q.popleft()
        # 맨 앞 요소보다 더 큰 요소가 뒤에 있는 경우 다시 뒤에 append 한다.
        # any(item[0] < que[0] for que in q) 으로도 풀 수 있다. any라는 함수는 그 중에 어느 하나라도 조건을 만족하는 것을 판별한다.
        if q and max(q)[0] > item[0]:
            q.append(item)
        else:
            answer += 1
            # 현 인덱스가 찾는 위치인 경우
            if item[1] == location:
                break
    return answer