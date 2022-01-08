import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)
maxRes=[0,0,0]
minRes=[0,0,0]
for _ in range(int(input())):
    a,b,c=map(int,input().split())

    #maxRes
    maxRes[:]=[max(maxRes[0]+a,maxRes[1]+a),max(maxRes[0]+b,maxRes[1]+b,maxRes[2]+b),max(maxRes[1]+c,maxRes[2]+c)] 
    #https://stackoverflow.com/questions/7677275/list-assignment-with    

    #minRes
    minRes[:]=[min(minRes[0]+a,minRes[1]+a),min(minRes[0]+b,minRes[1]+b,minRes[2]+b),min(minRes[1]+c,minRes[2]+c)]

print(max(maxRes),min(minRes))


