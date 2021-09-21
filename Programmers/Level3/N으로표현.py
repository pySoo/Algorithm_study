# https://programmers.co.kr/learn/courses/30/lessons/42895
"""
문제
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.

입출력
N	number	return
5	12	4
2	11	3
"""


def solution(N, number):
    S = [0, {N}]
    if N == number:
        return N % number + 1
    for i in range(2, 9):
        # i=2: n을 두 번 사용하는 연산일 경우 n*2 = {nn}
        possible_set = {int(str(N)*i)}
        for i_half in range(1, i//2+1):
            # S[i_half] 연산 S[i-i_half], 예: S[1] 연산 S[3] = N을 4번 썼을 때 가능한 집합
            for x in S[i_half]:
                for y in S[i-i_half]:
                    possible_set.add(x+y)
                    possible_set.add(x-y)
                    possible_set.add(x*y)
                    if x != 0:
                        possible_set.add(y//x)
                    if y != 0:
                        possible_set.add(x//y)
        if number in possible_set:
            return i
        S.append(possible_set)
    return -1
