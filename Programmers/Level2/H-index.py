# h편 이상 인용된 논문이 h개 이상이 되는 h의 최대값을 찾는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42747
# 원소가 [1,2,2,3,3,3]이 있을 때, 1편 이상 인용된 논문 1개 이상, 2편 이상 인용된 논문 2편 이상을 만족하지만
# 1과 2를 초과하는 원소가 있습니다. 3편 이상 인용된 논문도 3개 이상이므로 답은 최대값 3이 됩니다.
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        h = citations[i]
        if h >= l-i:
            return l-i
        
    return 0