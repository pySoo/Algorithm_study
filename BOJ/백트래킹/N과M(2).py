# https://www.acmicpc.net/problem/15650
"""
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""
n, m = list(map(int, input().split()))

check_list = []
output = []


def dfs(depth):
    if depth == m:
        print(' '.join(map(str, output)))
        return

    for i in range(n):
        if check_list[i]:
            continue
        check_list[i] = True
        output.append(i+1)
        dfs(depth+1)
        output.pop()

        # (1)문제의 순열과 차이점이다
        # output 마지막 요소 삭제 후 해당 요소 뒤에 있는 요소들은 모두 False 처리
        # 마지막에 돌아왔을 때 맨 앞의 자리는 True가 되어, 다음 loop에서 접근하지 못하게 하기 위함이다.
        # 참고한 블로그 https://hwan-hobby.tistory.com/261
        for j in range(i+1, n):
            check_list[j] = False


dfs(0)
