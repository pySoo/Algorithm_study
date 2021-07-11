# 2020 카카오 블라인드
# 연속되는 같은 문자는 (연속된 개수+문자)로 압축하여 만들 수 있는 최소한의 길이를 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/60057
# abcabc라는 문자가 있을 때 길이의 절반(4 이상)을 넘어가는 길이는 비교하지 않도록 하였습니다.
def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2 + 1):
        temp = ''
        cnt = 1
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+i+i]:
                cnt += 1
            else:
                if cnt > 1:
                    temp += str(cnt)
                    cnt = 1
                    
                temp += s[j:j+i]
        if answer > len(temp):
            answer = len(temp)
    return answer