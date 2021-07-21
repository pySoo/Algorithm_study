# 사람들의 몸무게를 한계값을 넘지 않도록 조합하여 최소한의 구명보트를 사용하는 문제
# https://programmers.co.kr/learn/courses/30/lessons/42885

# 처음에는 sort()이후 pop()연산을 이용해서 리스트의 원소가 없어질 때까지 계산하였는데 효율성에서 문제가 발생했습니다.
# start와 end 인덱스를 이용하여 값을 비교하도록 하여 문제를 해결했습니다.
# 구명보트에 최대 2명까지만 탈 수 있다는 조건으로 마지막 원소와 첫 원소만 비교하여 비교적 간단하게 풀 수 있었습니다.
def solution(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) - 1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        answer += 1
        end -= 1
        
    return answer