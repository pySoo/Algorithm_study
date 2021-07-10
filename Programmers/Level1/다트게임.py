# 정해진 규칙에 따라서 다트 게임 점수를 계산하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/17682
# 위 문제를 풀면서 배운 점은 dictionary 활용 방법과 문자열 예외처리 방법입니다.
# 문자열 원소 하나씩 비교하며 계산하였는데 유일한 두 자리수인 10을 처리할 때 문제가 발생했습니다.
# 이 문제는 10이라는 문자열을 k로 치환해서 따로 처리해주었습니다.

def solution(dartResult):
    answer = []
    stage = -1
    dartResult = dartResult.replace('10','K')
    sdt = {'S' : 1, 'D' : 2, 'T' : 3}
    for s in dartResult:
        if s in sdt:
            answer[stage] **= (sdt[s])
        elif s == '*':
            answer[stage] *= 2
            if stage != 0:
                answer[stage-1] *= 2
        elif s == '#':
                answer[stage] *= -1
        else:
            s = 10 if s == 'K' else int(s)
            answer.append(s)
            stage += 1
            
    return sum(answer)