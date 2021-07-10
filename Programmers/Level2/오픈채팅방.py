# 2019 카카오 블라인드
# userid로만 유저 구분이 가능하고 닉네임 변경, 방 나가기 등을 고려하여 최종적으로 보이는 이름을 출력하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42888

# 처음에는 userid를 문자열에 넣고 마지막에 모든 answer를 돌며 닉네임으로 변환하도록 풀었는데
# replace를 쓰지 않고 record를 다시 도는 것이 속도가 빠르고 간결하여서 다른 분의 풀이를 참고하였습니다.
def solution(record):
    answer = []
    user = {}
    
    for sentence in record:
        s = sentence.split()
        if s[0] == 'Enter' or s[0] == 'Change':
            user[s[1]] = s[2]
    
    for sentence in record:
        s = sentence.split()
        if s[0] == 'Enter':
            answer.append(user[s[1]]+'님이 들어왔습니다.')
        elif s[0] == 'Leave':
            answer.append(user[s[1]]+'님이 나갔습니다.')
            
    return answer