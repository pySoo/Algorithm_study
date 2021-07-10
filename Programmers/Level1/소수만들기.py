# 조합을 만들어 그 합이 소수인지 판별하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations
import math

def isPrime(n):
    sqrt = math.sqrt(n)

    # 에라토스테네스의 체에 의해 제곱근까지만 나눠보면 소수인지 판별이 가능하다.
    for i in range(2, int(sqrt+1)):
        if n % i == 0:
            return False
    return  True

def solution(nums):
    answer = 0
    combi = list(combinations(nums,3))
    
    for n1,n2,n3 in combi:
        if isPrime(n1+n2+n3):
            answer += 1

    return answer