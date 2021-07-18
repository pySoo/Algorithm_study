# 2021 카카오 블라인드
# https://programmers.co.kr/learn/courses/30/lessons/72412
# 4가지 조건과 점수가 담긴 질의문을 만족하는 지원자 수를 구하는 문제
# 중요한 점: 해시맵) 4가지 조건에 대한 2^4개의 경우를 key로 설정하고, 점수를 value로 설정한 dictionary를 만듭니다.
# 점수를 오름차순 정렬하여 binary 탐색으로 만족하는 지원자를 찾는 것이 효율성 문제를 통과하는 방법입니다.

# 처음 풀이에서는 사용 언어를 key 값으로 설정하여 다시 그 안에서 문자열을 비교하여 찾도록 하였는데 효율성을 통과하지 못했습니다. 
# 카카오 문제 해설을 참고한 바 binary 탐색으로 해결하는 것이 핵심이었습니다.
# 위 문제를 풀면서 배운 점은 binary 탐색 활용 방법과 문자열로 조합을 만들어 dictionary의 key로 설정하여 해시맵을 활용한 방법입니다.

from itertools import combinations
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            # 하나의 info에서 경우의 수 16개 만들기 -> 항목이 4개이므로
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)
    for key in info_dict.keys():
        # lower bound 사용하기 위해 점수를 오름차순으로 정렬
        info_dict[key].sort()
    
    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]
        
        # and 제거
        for i in range(3):
            query.remove('and')
        
        while '-' in query:
            query.remove('-')
        # 리스트를 문자열로
        tmp_q = ''.join(query)
        
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer
    