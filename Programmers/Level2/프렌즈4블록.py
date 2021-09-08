# https://programmers.co.kr/learn/courses/30/lessons/17679
"""
문제
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.\
블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

입출력
m	n	board	answer
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
"""
from collections import deque


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        checked = []
        for i in range(m - 1):
            for j in range(n - 1):
                # 이미 블록이 터짐
                if board[i][j] == "0":
                    continue
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    checked.append((i, j))
                    checked.append((i, j + 1))
                    checked.append((i + 1, j))
                    checked.append((i + 1, j + 1))
        # 이번에 터진 블록이 없으면 종료
        if len(checked) == 0:
            break
        else:
            answer += len(set(checked))
            for c in checked:
                board[c[0]][c[1]] = '0'

            # 같은 행의 열들을 검사해서  터진 자리 위에 있는 블록들을 내린다.
            for c in reversed(checked):   # 블록들 내리기
                down_n = c[0] - 1
                now_n = c[0]

                while down_n >= 0:
                    if board[now_n][c[1]] == '0' and board[down_n][c[1]] != '0':
                        board[now_n][c[1]] = board[down_n][c[1]]
                        board[down_n][c[1]] = '0'
                        now_n -= 1
                    down_n -= 1
    return answer
