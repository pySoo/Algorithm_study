# Greedy 알고리즘, 중복처리를 set으로 해결
# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    # 여벌 체육복 있는 학생도 도난 당했을 수 있다
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    # Greedy: 여벌 체육복 있는 학생은 왼쪽부터 빌려주어야 최적의 해에 가까워짐
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
        
    return n-len(set_lost)