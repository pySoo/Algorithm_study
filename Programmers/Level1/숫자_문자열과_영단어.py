# 2021 카카오 인턴쉽
# 문자와 숫자가 섞여있는 문자열을 변환하여 숫자로 바꾸는 문제
# https://programmers.co.kr/learn/courses/30/lessons/81301
# 처음엔 문자와 숫자 배열을 2개 만들어서 비교하여 풀었으나 파이썬의 dictionary를 활용하는 좋은 풀이가 있어서 참고하였습니다.
# items() 함수를 이용해서 key 값으로 값을 찾아 문자열을 숫자로 변환하였습니다. 아직은 갈 길이 먼 것 같지만.. 파이썬 라이브러리 알아갈수록 너무 재밌습니다^^
def solution(s):
    num_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)