# https://www.acmicpc.net/problem/2873
"""
문제
상근이는 우리나라에서 가장 유명한 놀이 공원을 운영하고 있다. 이 놀이 공원은 야외에 있고, 다양한 롤러코스터가 많이 있다.
어느 날 벤치에 앉아있던 상근이는 커다란 황금을 발견한 기분이 들었다. 자신의 눈 앞에 보이는 이 부지를 구매해서 롤러코스터를 만든다면, 세상에서 가장 재미있는 롤러코스터를 만들 수 있다고 생각했다.
이 부지는 직사각형 모양이고, 상근이는 R행 C열의 표 모양으로 나누었다. 롤러코스터는 가장 왼쪽 위 칸에서 시작할 것이고, 가장 오른쪽 아래 칸에서 도착할 것이다. 롤러코스터는 현재 있는 칸과 위, 아래, 왼쪽, 오른쪽으로 인접한 칸으로 이동할 수 있다. 각 칸은 한 번 방문할 수 있고, 방문하지 않은 칸이 있어도 된다.
각 칸에는 그 칸을 지나갈 때, 탑승자가 얻을 수 있는 기쁨을 나타낸 숫자가 적혀있다. 롤러코스터를 탄 사람이 얻을 수 있는 기쁨은 지나간 칸의 기쁨의 합이다. 가장 큰 기쁨을 주는 롤러코스터는 어떻게 움직여야 하는지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 R과 C가 주어진다. (2 ≤ R, C ≤ 1000) 둘째 줄부터 R개 줄에는 각 칸을 지나갈 때 얻을 수 있는 기쁨이 주어진다. 이 값은 1000보다 작은 양의 정수이다.

출력
첫째 줄에 가장 가장 큰 기쁨을 주는 롤러코스터는 가장 왼쪽 위 칸부터 가장 오른쪽 아래 칸으로 어떻게 움직이면 되는지를 출력한다. 위는 U, 오른쪽은 R, 왼쪽은 L, 아래는 D로 출력한다. 정답은 여러 가지 일 수도 있다.
"""
import sys

def printCodd():
    for i in range(c//2):
        print("D"*(r-1),end="")
        print("R",end="")
        print("U"*(r-1),end="")
        print("R",end="")
    print("D"*(r-1))

def printRoddCeven():
    for i in range(r//2):
        print("R"*(c-1),end="")
        print("D",end="")
        print("L"*(c-1),end="")
        print("D",end="")
    print("R"*(c-1))

def printRevenCeven(temps):
    min = 1000
    indexi=-1
    indexj=-1
    for i in range(r):
        for j in range(c):
            if((i+j)%2!=0 and min>temps[i][j]):
                min=temps[i][j]
                indexi=i
                indexj=j
    res = ('D'*(r-1)+'R'+'U'*(r-1)+'R')*(indexj//2)
    currentX=2*(indexj//2)
    currentY=0
    xbound=2*(indexj//2)+1
    while currentX!=xbound or currentY!=r-1:
        if(currentX<xbound and [currentY,xbound]!=[indexi,indexj]):
            currentX+=1
            res+='R'
        elif currentX == xbound and [currentY, xbound - 1] != [indexi,indexj]:
            currentX -= 1
            res += 'L'
        if currentY != r - 1:
            currentY += 1
            res += 'D'
    res += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - indexj - 1) // 2)
    print(res)

r, c = map(int, sys.stdin.readline().rstrip("\n").split())
nums = []
for i in range(r):
    nums.append(list(map(int, sys.stdin.readline().rstrip().split())))
start=nums[0][0]
end=nums[r-1][c-1]
temps=nums[:]
if(c%2!=0):
    printCodd()
elif(r%2!=0):
    printRoddCeven()
elif(c%2==0 and r%2==0):
    printRevenCeven(temps)
    