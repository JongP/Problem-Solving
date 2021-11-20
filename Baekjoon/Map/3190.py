from collections import deque
import sys
input = sys.stdin.readline



n = int(input())
board=[[-1]*(n+1) for _ in range(n+1)]
board[1][1]=0
head=(1,1)
tail=(1,1)

k = int(input())
for _ in range(k):
    x,y = map(int,input().rstrip().split())
    board[x][y]=4  # 4 for apple

l = int(input())
commands = deque([])
for _ in range(l):
    x,c = input().rstrip().split()
    commands.append((int(x),c))


clock = 0

dxy = [(0,1),(-1,0),(0,-1),(1,0)]


while True:
    clock+=1
    #print(head)
    xHead ,yHead = head
    toward = board[xHead][yHead]

    next_xHead , next_yHead = (xHead+dxy[toward][0],yHead+dxy[toward][1])
    #print(clock, next_xHead,next_yHead,toward)

    if commands and commands[0][0] == clock:
        _, c = commands.popleft()
        if c == "L":
            toward = (toward+1)%4
        elif toward == 0:
            toward = 3
        else:
            toward = (toward-1)%4    

    if next_xHead<1 or next_xHead>n or next_yHead<1 or next_yHead>n or board[next_xHead][next_yHead] in [0,1,2,3]:
        break
    elif board[next_xHead][next_yHead] == -1 :
        towardTail = board[tail[0]][tail[1]]
        board[tail[0]][tail[1]] = -1
        tail = (tail[0]+dxy[towardTail][0],tail[1]+dxy[towardTail][1])
    board[next_xHead][next_yHead] = toward
    head = (next_xHead,next_yHead)

    #print("command: ",commands[0])


    #print(clock,":", next_xHead,next_yHead,toward)
#    for row in board:
 #       print(row)
 #   print("\n")



print(clock)