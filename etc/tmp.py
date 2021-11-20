def solution(A):
# write your code in Python 3.6
    answer=-1
    myDict={}
    for i in range(l):
        if A[i] not in myDict:
            myDict[A[i]]=[i,-1] 
        else:
            myDict[A[i]][1]=i

    for num in myDict:
        if myDict[num][1]==-1:
            continue
        else:
            answer=max(answer,sum(A[myDict[num][0]:myDict[num][1]+1]))


    return answer