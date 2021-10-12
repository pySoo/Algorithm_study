# https://programmers.co.kr/learn/courses/30/lessons/67258
"""
- 문제
[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

개발자 출신으로 세계 최고의 갑부가 된 어피치는 스트레스를 받을 때면 이를 풀기 위해 오프라인 매장에 쇼핑을 하러 가곤 합니다.
어피치는 쇼핑을 할 때면 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있습니다.
어느 날 스트레스를 풀기 위해 보석 매장에 쇼핑을 하러 간 어피치는 이전처럼 진열대의 특정 범위의 보석을 모두 구매하되 특별히 아래 목적을 달성하고 싶었습니다.
진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다. 이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return 하도록 solution 함수를 완성해주세요.
가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며, 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.

- 제한사항
gems 배열의 크기는 1 이상 100,000 이하입니다.
gems 배열의 각 원소는 진열대에 나열된 보석을 나타냅니다.
gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있습니다.
gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열입니다.
"""
# 투 포인터 이용 구간 탐색 문제
# 배열 크기가 최대 100000이므로 O(n^2) 이상인 탐색 알고리즘으로는 풀이가 불가능하다.
# O(n)의 투 포인터 알고리즘을 사용해야한다.


def solution(gems):
    answer = [1, len(gems)]
    start, end = 0, 0
    gems_len = len(set(gems))
    # 구간 내의 보석 개수
    shortest = len(gems)
    # 보석 종류별 개수를 저장하는 딕셔너리
    my_gems = {}

    while end < len(gems):
        if gems[end] not in my_gems:
            my_gems[gems[end]] = 1
        else:
            my_gems[gems[end]] += 1
        end += 1
        # 포함해야 하는 보석을 모두 가지고 있을 때
        if len(my_gems) == gems_len:
            while start < end:
                # 하나 이상 존재하면 뒤에도 같은 보석이 존재하므로 start 포인터를 한 칸 이동
                if my_gems[gems[start]] > 1:
                    my_gems[gems[start]] -= 1
                    start += 1
                # 현 구간이 더 짧으면 answer 갱신
                elif end - start < shortest:
                    shortest = end - start
                    answer = [start+1, end]
                    break
                else:
                    break

    return answer
