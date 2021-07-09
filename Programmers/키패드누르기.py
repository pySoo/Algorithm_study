# 키패드 상의 거리를 비교하여 왼,오른손 잡이에 따라 다르게 처리하는 문제
# 좌우 1, 상하 3차이의 규칙을 이용하여 3으로 나눈 몫과 나머지로 거리를 계산하는 아이디어를 생각하는게 관건인 것 같다..
# 실제 시험에서 생각이 나지 않는다면 좌표를 지정해서 계산하는게 좋을 것이라 생각한다.
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    nLeft, nRight = 10, 12
    
    for n in numbers:
        if n in left:
            answer += 'L'
            nLeft = n
        elif n in right:
            answer += 'R'
            nRight = n
        else:
            # 0의 경우 거리 계산을 위해 예외처리
            if n == 0:
                n = 11
            # 위아래는 3차이가 나고 좌우는 1차이가 난다.
            # 원소간 차를 3으로 나누어서 몫과 나머지의 합으로 거리를 구해야 함.
            # 예) 2에서 9까지의 경우, 7//3 + 7%3 -> 3 (거리차)
            l_dis = sum(divmod(abs(nLeft - n),3))
            r_dis = sum(divmod(abs(nRight - n),3))
            
            if l_dis == r_dis:
                if hand == 'left':
                    answer += 'L'
                    nLeft = n
                else:
                    answer += 'R'
                    nRight = n
            elif l_dis < r_dis:
                answer += 'L'
                nLeft = n
            else:
                answer += 'R'
                nRight = n
            
    return answer

    # 좌표로 거리를 계산한 다른 분의 풀이
    # def solution(numbers, hand):
    # answer = ''
    # location = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    # left, right = [3, 0], [3, 2]
    #
    # for i in numbers:
    # 무조건 L,R에 들어갈 값을 지정하지 않고 몫과 나머지로 계산하여 처리하셨다. 좋은 풀이라고 생각한다!
    #     if i % 3 == 1:
    #         answer += 'L'
    #         left = location[i]
    #     elif i % 3 == 0 and i != 0:
    #         answer += 'R'
    #         right = location[i]
    #     else:
    #         l = abs(location[i][0] - left[0]) + abs(location[i][1] - left[1])
    #         r = abs(location[i][0] - right[0]) + abs(location[i][1] - right[1])
    #         if l < r:
    #             answer += 'L'
    #             left = location[i]
    #         elif l > r:
    #             answer += 'R'
    #             right = location[i]
    #         else:
    #             answer += hand[0].upper()
    #             if hand == 'right':
    #                 right = location[i]
    #             else:
    #                 left = location[i]                

    # return answer