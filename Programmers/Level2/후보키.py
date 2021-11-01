# https://programmers.co.kr/learn/courses/30/lessons/42890
"""
문제
프렌즈대학교 컴퓨터공학과 조교인 제이지는 네오 학과장님의 지시로, 학생들의 인적사항을 정리하는 업무를 담당하게 되었다.

그의 학부 시절 프로그래밍 경험을 되살려, 모든 인적사항을 데이터베이스에 넣기로 하였고, 이를 위해 정리를 하던 중에 후보키(Candidate Key)에 대한 고민이 필요하게 되었다.

후보키에 대한 내용이 잘 기억나지 않던 제이지는, 정확한 내용을 파악하기 위해 데이터베이스 관련 서적을 확인하여 아래와 같은 내용을 확인하였다.

관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.

제한사항
relation은 2차원 문자열 배열이다.
relation의 컬럼(column)의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
relation의 로우(row)의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
relation의 모든 문자열의 길이는 1 이상 8 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)

입출력
relation	result
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	2
"""

"""
알고리즘
1. 1부터 column 수만큼 column에 관한 조합 생성 (0,) (0,1) 등
2. 유일성 검사: 튜플에 대해 중복을 제거해도 모든 행의 데이터가 존재할 때 만족
3. 최소성 검사: 유일성을 만족하는 현 요소와 다음 요소가 겹치는 것이 있을 때 만족하지 않음
"""




from itertools import combinations
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for i in range(1, col+1):
        candidates.extend(combinations(range(col), i))

    # 유일성 검사
    unique = []
    for col in candidates:
        tmp = []
        for item in relation:
            tmp.append(tuple(item[i] for i in col))
            # 중복을 제거해도 모든 행의 데이터가 있을 때 유일성 만족
            if len(set(tmp)) == row:
                # 유일성 만족하는 컬럼 저장
                unique.append(col)

    # 최소성 검사
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            # 현 요소 길이와 다음 요소들과의 교집합 길이가 같다면 겹치는 것
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                # 집합에서 해당 요소를 제거한다.
                answer.discard(unique[j])
    return len(answer)
