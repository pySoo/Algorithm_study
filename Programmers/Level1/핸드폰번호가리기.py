# 뒤 4자리 수를 제외한 번호를 가리는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12948
# 파이썬의 리스트의 음수 인덱스를 앞에 배치하면, 뒤에서부터 문자열을 가져올 수 있게 합니다.
def solution(phone_number):
    n = len(phone_number)
    # 뒤에서 4번째부터 마지막 원소까지 저장
    back = phone_number[-4:]
    return "*" * (n - 4) + back