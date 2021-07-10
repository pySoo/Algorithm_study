# 알고 있는 로또 번호와 모르는 번호를 유추하여 최고, 최저 순위를 알아내는 문제
# https://programmers.co.kr/learn/courses/30/lessons/77484
# 처음에는 단순 if 문으로 풀었으나 rank 인덱스로 순위를 구할 수 있는 풀이가 있길래 참고하였습니다.
# 이 문제에서는 특정 원소의 개수를 알아낼 수 있는 count 함수를 알게 되었습니다.
def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]

    # 0이 있으면 무조건 일치로 변경할 수 있으므로 카운트
    cnt_zero = lottos.count(0)
    correct = 0
    for n in win_nums:
        if n in lottos:
            correct += 1
    return rank[correct + cnt_zero],rank[correct]
