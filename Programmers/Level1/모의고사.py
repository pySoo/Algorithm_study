# 일정한 패턴으로 문제를 찍을 때 가장 많이 맞춘 사람을 구하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    counts = [0,0,0]
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        # 배열값보다 클 경우 나머지를 이용하여 반복 계산을 하도록 한다
        if answers[i] == n1[i%5]:
            counts[0] += 1
        if answers[i] == n2[i%8]:
            counts[1] += 1
        if answers[i] == n3[i%10]:
            counts[2] += 1
            
    for i in range(3):
        if counts[i] == max(counts):
            answer.append(i+1)
    return answer