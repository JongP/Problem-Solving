import sys
input = sys.stdin.readline

#return next_bottom and next_right_side
def next_dice(dice,command):
    if command == 1:
        tmp = dice[0]
        dice[0]=dice[2]
        dice[2]=dice[5]
        dice[5]=dice[3]
        dice[3] = tmp
    elif command ==2 :
        tmp = dice[0]
        dice[0]=dice[3]
        dice[3]=dice[5]
        dice[5]=dice[2]
        dice[2]=tmp
    elif command ==3 :
        tmp=dice[0]
        dice[0]=dice[1]
        dice[1]=dice[5]
        dice[5]=dice[4]
        dice[4]=tmp
    elif command ==4 :
        tmp=dice[0]
        dice[0]=dice[4]
        dice[4]=dice[5]
        dice[5]=dice[1]
        dice[1]=tmp


dice =[0]*6

n,m, x, y, k = map(int,input().rstrip().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip().split())))

commands = list(map(int,input().rstrip().split()))

ansList=[]

def print_all():
    for row in graph:
        print(row)
    print("dice",x,y)
    print(dice)
    print("\n")
#print_all()
for command in commands:
    #can't move, otherwise move
    if command==1 :
        if y==m-1: continue
        y+=1
    elif command==2 :
        if y==0: continue
        y-=1
    elif command==3:
        if x==0: continue
        x-=1
    elif command==4 :
        if x==n-1: continue
        x+=1

    next_dice(dice,command)

    if graph[x][y]==0:
        graph[x][y] = dice[0]
    else:
        dice[0] = graph[x][y]
        graph[x][y] = 0
    #print_all()
    ansList.append(dice[5])

for answer in ansList:
    print(answer)