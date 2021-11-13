# https://programmers.co.kr/learn/courses/30/lessons/42627
"""
문제
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.
예)
- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

입출력
jobs	return
[[0, 3], [1, 9], [2, 6]]	9
"""
"""
알고리즘
1. 현 시점에서 처리 가능한 작업을 힙에 삽입
- 처리 가능한 작업: 작업 요청 시간이 이전 작업 시작 시간(start)보다 크고 현 시점(now)보다 작거나 같을 때 힙에 삽입
2. 소요시간 기준으로 최소힙 생성
3. 최소힙에서 pop한 후에(실행시간 가장 적은 요소가 나옴) 현 시간 변수들 갱신
4. 힙이 비었다면 현 시간 1 증가
"""




import heapq
def solution(jobs):
    answer, now, cnt = 0, 0, 0
    heap = []
    start = -1
    while cnt < len(jobs):
        for job in jobs:
            # 1
            if start < job[0] <= now:
                # 2
                heapq.heappush(heap, (job[1], job[0]))
        # 3
        if len(heap) > 0:
            heap_term, heap_start = heapq.heappop(heap)
            start = now
            now += heap_term
            answer += (now - heap_start)
            cnt += 1
        # 4
        else:
            now += 1
    return answer//len(jobs)
