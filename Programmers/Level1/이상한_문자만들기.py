# 짝수 원소는 대문자로, 홀수는 소문자로 만드는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    words_list = s.split(' ') 
    new_list = []
    for word in words_list: 
        words = ''
        # 파이썬의 문자열은 인덱스로 접근해서 변경하는 것이 불가능하기 때문에 리스트에 새로운 문자열을 더하였습니다.
        for i in range(len(word)):
            words += word[i].upper() if i%2 == 0 else word[i].lower() 
        new_list.append(words)
    return ' '.join(new_list)