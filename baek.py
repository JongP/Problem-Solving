import sys
input = sys.stdin.readline

n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().rstrip().split())))