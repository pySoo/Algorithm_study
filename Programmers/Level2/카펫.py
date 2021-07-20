# 중앙에 노란색을 포함한 갈색 카펫의 가로, 세로 길이를 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    sums = brown + yellow
    # 약수를 구하는 방식으로 해가 풀이되므로 에라토스테네스의 체를 이용하여
    # 범위를 제곱근 이내로 만들어 시간을 단축시켰습니다.

    # 알고리즘을 풀 때 단위를 작게 만들어서 분석하는 것이 중요하다고 느꼈습니다.
    # 3x4 사각형이 있을 때, 내부 사각형의 크기는 (3-2) x (4-2)의 형태가 되는 것을 이용했습니다.
    for i in range(sums,int(yellow ** 0.5)-1,-1):
        if sums % i == 0:
            a = sums // i
            if (a-2) * (i-2) == yellow:
                return [i, a]