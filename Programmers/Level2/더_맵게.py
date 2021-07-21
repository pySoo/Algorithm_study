# 스코빌 지수가 가장 낮은 2개를 조합하여 모두 K이상으로 만드는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42626

# sort() 후에 맨 앞 원소 2개를 조합해서 풀이했으나 시간 초과가 발생했습니다.
# 이번 문제를 풀이하면서 배운 점은 heap 자료구조는 push, pop 연산마다 자동으로 정렬한다는 것입니다.
# 앞서 문제였던 정렬 비용을 감소시킴으로써 효율성 문제를 해결하였습니다.
import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    # 인덱스 에러 문제를 try, except문으로도 풀 수 있다는 것을 알게 됐습니다.
    while heap[0] < K:
        first = heapq.heappop(heap)
        if len(heap) == 0:
            return -1
        second = heapq.heappop(heap)
        heapq.heappush(heap, first + second * 2)
        answer += 1
    return answer