# 주어진 문자열로 조합할 수 있는 수들 중 몇 개가 소수인지 찾는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42839
# permutations 활용법을 알게 되었습니다. 문자열을 이용하면 ('1','7')과 같은 튜플 형식으로 만들어지는데,
# 이를 한 문자열로 만들기 위해 ''.join()을 사용하였고, map 함수를 통해 정수로 치환하였습니다.
# 효율성 부문을 통과하기 위해 set을 통해 중복을 제거하였고 소수 계산 범위를 제곱근으로 설정하였습니다.
from itertools import permutations
def isPrime(n):
    if n in (0,1):
        return False
    sqrt = n ** 0.5
    for i in range(2, int(sqrt) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    p, check = [], []
    for i in range(1, len(numbers) + 1):
        temp = list(map(int,map(''.join, permutations(numbers,i))))
        p.extend(temp)
        
    p = list(set(p))

    for n in p:
        if isPrime(n) and n not in check:
            check.append(n)
    
    return len(check)