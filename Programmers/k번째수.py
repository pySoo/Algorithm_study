# 배열 활용 기본 문제
# array의 i번째 숫자부터 j번째 숫자까지 정렬했을 때, k번째 있는 수를 구함

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command[0],command[1],command[2]
        slice = array[i-1:j]
        slice.sort()
        answer.append(slice[k-1])
    return answer
    #return [sorted(array[i-1:j])[k-1] for i,j,k in commands]
    #List Comprehension을 사용한 pythonic한 풀이이다.