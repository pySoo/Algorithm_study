# 범위 내에 있는 소수의 개수를 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/12921
# 간단한 문제 같지만 효율성 문제로 인해서 애를 먹었다. 먼저 n+1개의 배열을 모두 true로 설정하고 for문의 범위를 sqrt(n)으로 설정한다.
# 범위 내 숫자들의 배수를 모두 false로 만들어서 true인 요소의 개수를 구하여 해결하였다.
def solution(n):
    arr = [True] * (n+1)
    m = int(n**0.5)
    for i in range(2, m + 1):
        if arr[i] == True:
            for j in range(i+i, n+1, i):
                arr[j] = False
    return len([i for i in range(2, n+1) if arr[i] == True])