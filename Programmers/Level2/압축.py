# https://programmers.co.kr/learn/courses/30/lessons/17684
"""
문제
신입사원 어피치는 카카오톡으로 전송되는 메시지를 압축하여 전송 효율을 높이는 업무를 맡게 되었다. 메시지를 압축하더라도 전달되는 정보가 바뀌어서는 안 되므로, 압축 전의 정보를 완벽하게 복원 가능한 무손실 압축 알고리즘을 구현하기로 했다.
어피치는 여러 압축 알고리즘 중에서 성능이 좋고 구현이 간단한 LZW(Lempel–Ziv–Welch) 압축을 구현하기로 했다. LZW 압축은 1983년 발표된 알고리즘으로, 이미지 파일 포맷인 GIF 등 다양한 응용에서 사용되었다.

LZW 압축은 다음 과정을 거친다.

길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
단계 2로 돌아간다.

주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.

입출력
msg	answer
KAKAO	[11, 1, 27, 15]
TOBEORNOTTOBEORTOBEORNOT	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
ABABABABABABABAB	[1, 2, 27, 29, 28, 31, 30]
"""
# 나의 풀이, 스택을 이용해 좁은 범위에서 넓은 범위로 비교하였기 때문에 아래의 풀이와 비교하였을 때 시간이 최대 90ms 단축되었다고 생각한다.
# 그렇지만 이중 while문을 쓰는 것이 아쉬워서 다른분의 인덱스 활용 풀이를 참고하여 공부하였다.
from collections import defaultdict


def solution(msg):
    answer = []
    dic = defaultdict(int)
    stack = list(msg)
    for i in range(1, 27):
        dic[chr(64+i)] = i

    start = 0
    end = len(msg)
    while stack:
        w = stack.pop(0)
        c = stack[0] if stack else '_'
        while w+c in dic:
            w = w+c
            stack.pop(0)
            c = stack[0] if stack else '_'
        if w+c not in dic:
            dic[w+c] = len(dic) + 1
        answer.append(dic[w])
    return answer


def solution(msg):
    answer = []
    dic = defaultdict(int)
    stack = list(msg)
    for i in range(1, 27):
        dic[chr(64+i)] = i

    start = 0
    end = len(msg)
    while True:
        w = msg[start:end]
        if w in dic.keys():
            answer.append(dic[w])
            if end >= len(msg):
                return answer
            c = msg[end]
            dic[w+c] = len(dic) + 1
            start += len(w)
            end = len(msg)
        else:
            end -= 1
