#징검다리
#https://programmers.co.kr/learn/courses/30/lessons/43236


def isPossible(mid):
    global dists,limit,lenDist
    localDists=dists[:]
    cnt=0

    for i in range(lenDist):
        if localDists[i]<mid:
            if cnt==limit:
                return False
            if(i==lenDist-1):
                tmp=localDists[i-1]+localDists[i]
                if tmp<mid:
                    return False

            cnt+=1
            localDists[i+1]=localDists[i]+localDists[i+1]
    return True


def solution(distance, rocks, n):
    answer = 0
    global dists,limit,lenDist
    limit=n

    rocks.append(0)
    rocks.append(distance)



    rocks.sort()
    dists=[]
    le=int(2e9)
    ri=distance//(len(rocks)-2-n+1)+1

    for i in range(0,len(rocks)-1):
        dists.append(rocks[i+1]-rocks[i])
        if(rocks[i+1]-rocks[i]<le):
            le=rocks[i+1]-rocks[i]

    lenDist=len(dists)

    #print(dists,le,ri)

    while(le<ri):
        mid=(le+ri+1)//2
        
        
        if isPossible(mid):
            le=mid
        else:
            ri=mid-1

    
    #print(le)
    return le


solution(25,[2, 14, 11, 21, 17],2)