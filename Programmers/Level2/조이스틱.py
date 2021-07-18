# 조이스틱을 최소한의 동작으로 조작하여 원하는 문자열을 만드는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42860
# 알파벳 변경시의 상하 조작, 좌우 인덱스 조작을 최소로 설정하는 것이 필요했습니다.
# 방문시에는 값을 0으로 설정하여 모두 방문한 경우 반복문을 탈출하게 하였습니다.

def solution(name):
    # 알파벳 변경시 필요한 조작 횟수
    change = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]
    answer = 0
    idx = 0
    
    while True:
        answer += change[idx]
        # 방문시에 값을 0으로 설정, 모두 방문했다면 answer값을 리턴합니다.
        change[idx] = 0
        if sum(change) == 0:
            return answer
        
        # 좌우 이동 방향 정하기
        left, right = 1, 1
        for l in range(1, len(name)):
            if change[idx-l] == 0: left += 1
            else: break
        for r in range(1, len(name)):
            if change[idx+r] == 0: right += 1
            else: break
                
        # 좌우 이동 비교해서 적은 횟수로 인덱스 이동
        # 왼쪽 이동시 인덱스에서 left 값을 빼주어야 합니다.
        answer += left if left < right else right
        idx += -left if left < right else right