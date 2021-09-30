import sys
import heapq
input = sys.stdin.readline

n = int(input())

indexList=[n-1]*n

numbers=[list(map(int,input().rstrip().split())) for _ in range(n)]


for _ in range(n):
    maxNum = numbers[indexList[0]][0]
    maxIdx = 0
    for i in range(n):
        if numbers[indexList[i]][i]>maxNum:
            maxNum=numbers[indexList[i]][i]
            maxIdx=i
    indexList[maxIdx]-=1

print(maxNum)