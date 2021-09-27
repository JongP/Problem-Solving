def horizontal_move(visited,visitedNum,l,leftEnd,leftCost,rightEnd,rightCost):
    horizontal_cost=0

    while visitedNum!=l:
        #going to right
        print(visited,leftEnd,rightEnd, visitedNum)
        if leftCost>rightCost:
            cur=rightEnd
            visited[cur]=1
            visitedNum+=1
            horizontal_cost+=rightCost

            i=(cur+1)%l
            while i!=cur:
                if(visited[i]==0):
                    rightEnd=i
                    break
                i = (i+1)%l
        elif leftCost<rightCost:
            cur=leftEnd
            visited[cur]=1
            visitedNum+=1
            horizontal_cost+=leftCost

            i=(cur-1)%l
            while i!=cur:
                if(visited[i]==0):
                    leftEnd=i
                    break
                i = (i-1)%l            
        else:
            print("can't happen")

        if(rightEnd>=cur):
            rightCost = rightEnd-cur
        else:
            rightCost = rightEnd-cur +l
        if(leftEnd<=cur):
            leftCost = cur-leftEnd
        else:
            leftCost = cur - leftEnd +l
    print("\n")
    return horizontal_cost

def solution(name):
    answer = 0

    smallA = ord('A')
    largeA = ord('Z')+1
    Z = ord('Z')
    l = len(name)

    visited=[0]*l
    visited[0]=1
    if name[0]=='A':
        visitedNum=0
    else:
        visitedNum=1
    rightEnd=-1
    leftEnd=-1



    #vertical movement
    for i in range(l):
        char=name[i]
        if(char=='A'):
            visited[i]=1
            visitedNum+=1
            continue
        elif rightEnd==-1 and i!=0:
            rightEnd=i#가장 먼저 A가 나오지 않을 때
        leftEnd=i #마지막으로 A 아닌 문자가 나오는 순간

        asc=ord(char)
        answer+=min(asc-smallA,largeA-asc)
    
    if rightEnd==-1:#한 문자('A','F') 또는 전체 문자 A일때
        return answer

    
    #처음 순간
    cur = 0

    rightCost = rightEnd
    leftCost = l-leftEnd

    horizontal_cost =0


    print(visitedNum)
    if rightCost==leftCost:
        horizontal_cost=horizontal_move(visited,visitedNum,l,leftEnd,leftCost+1,rightEnd,rightCost)
        #goLeft=horizontal_move(visited[:],visitedNum,l,leftEnd,leftCost,rightEnd,rightCost+1)
        #goRight=horizontal_move(visited,visitedNum,l,leftEnd,leftCost+1,rightEnd,rightCost)
        #print(goRight,goLeft)
        #horizontal_cost=min(goLeft,goRight)
    else:
        horizontal_cost=horizontal_move(visited,visitedNum,l,leftEnd,leftCost,rightEnd,rightCost)

    print(answer,horizontal_cost)
        
    answer+=horizontal_cost

    return answer

#print(solution("BBBAAAB"),"\n")#9
print(solution("ABABAAAAABA")) #11