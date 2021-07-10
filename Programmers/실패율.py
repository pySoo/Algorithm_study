# https://programmers.co.kr/learn/courses/30/lessons/42889
# 처음에는 count로 스테이지별 사람 수를 세었으나 O(n^2)라는 단점 때문에 step 딕셔너리를 만들어서 해결하였습니다.
# 그 결과 1000ms를 줄일 수 있었습니다. count 함수가 사용하기 간편하나 O(n)이라는 단점이 있기 때문에 효율성 부문에서 주의해야겠습니다.
def solution(N, stages):
    fail = {}
    step = {}
    rest = len(stages)
    for i in stages:
        if i != N+1:
            step[i] = step.get(i,0) +1
    
    for stage in range(1,N+1):
        # 도달하지 못한 경우 0으로 예외처리를 해주어야 합니다. 이것 때문에 계속 런타임 에러가 났습니다ㅠ
        if rest == 0:
            fail[stage] = 0
        else:
            count = step.get(stage,0)
            fail[stage] = count / rest
            rest -= count
    
    return sorted(fail, key=lambda x:fail[x], reverse=True)