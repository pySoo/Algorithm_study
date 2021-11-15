# https://programmers.co.kr/learn/courses/30/lessons/42579
"""
- 문제
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

- 제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
"""
"""
알고리즘
1. {[장르이름]: 재생 횟수} 딕셔너리를 생성
2. 1의 딕셔너리를 횟수에 따라 정렬, 장르 이름만 저장한 배열 생성
2. {[장르이름]:(재생 횟수, 인덱스)} 딕셔너리를 생성
3. 3의 딕셔너리를 횟수에 따라 정렬하고 2개까지의 인덱스를 정답 배열에 추가 
"""




from collections import defaultdict
from operator import itemgetter
def solution(genres, plays):
    answer = []
    genre_dic = defaultdict(int)
    play_dic = defaultdict(list)
    # 1
    for genre, play in zip(genres, plays):
        genre_dic[genre] += play

    # 2
    genre_rank = [name for name, play in sorted(
        genre_dic.items(), key=itemgetter(1), reverse=True)]

    # 3
    for i, (genre, play) in enumerate(zip(genres, plays)):
        play_dic[genre].append([play, i])

    # 4
    for genre in genre_rank:
        rank = [idx for play, idx in sorted(
            play_dic[genre], key=lambda x: x[0], reverse=True)[:2]]
        answer.extend(rank)
    return answer
