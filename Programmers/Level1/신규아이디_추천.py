# 2021 카카오 블라인드
# 단계별 문자열 활용, 라이브러리 활용 문제
# https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    #2단계
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
            
    #3단계
    while '..' in answer:
        answer = answer.replace('..','.')
        
    #4단계
    if answer[0] == '.' and len(answer) >= 2:
        answer=answer[1:]
            
    if answer[-1] == '.':
        answer=answer[:-1]
        
    #5단계
    if answer == '':
        answer = 'a'
    
    #6단계
    if len(answer) >=16 :
        answer=answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #7단계
    while len(answer)<3:
        answer+=answer[-1]
            
    return answer