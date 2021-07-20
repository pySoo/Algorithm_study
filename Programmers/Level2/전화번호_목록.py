# 다른 전화번호의 접두어가 되는 번호가 있는지 확인하는 문제 / 해시, 문자열 비교 두 가지 방법으로 풀 수 있습니다.
# https://programmers.co.kr/learn/courses/30/lessons/42577

# 해시: 배열의 첫 글자부터 순서대로 문자열에 추가해서 hash에 해당하는 값이 있는지 풀이
# 문자열 비교: zip(phone_book, phone_book[1:]) 와 str.startswith()을 이용하여 풀이
def solution(phone_book):
    hash_map = {}
    
    for phone_num in phone_book:
        hash_map[phone_num] = 1
    
    for phone_num in phone_book:
        s = ""
        for num in phone_num:
            s += num
            if s in hash_map and s != phone_num:
                return False
    return True

# 문자열 풀이, 문자열 길이 제한이 20자여서 startswith()의 시간 복잡도가 O(n)이 된다고 합니다.
# 앞선 해시 풀이보다 효율성이 좋아져서 대략 300ms 차이가 발생하였습니다.
# def solution(phone_book):
#     phone_book.sort()
#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         if p2.startswith(p1):
#             return False
#     return True