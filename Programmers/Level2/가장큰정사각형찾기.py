# https://programmers.co.kr/learn/courses/30/lessons/12905
"""
문제
1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)

제한사항
표(board)는 2차원 배열로 주어집니다.
표(board)의 행(row)의 크기 : 1,000 이하의 자연수
표(board)의 열(column)의 크기 : 1,000 이하의 자연수
표(board)의 값은 1또는 0으로만 이루어져 있습니다.

입출력
board	answer
[[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	9
[[0,0,1,1],[1,1,1,1]]	4
"""


def solution(board):
    n = len(board)
    m = len(board[0])

    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1, n):
        dp[i][0] = board[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer**2
