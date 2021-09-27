#https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = n
    
    i=0
    lost.sort()
    l1=len(lost)
    
    reserve=set(reserve)
    taken=set()

    #자기 거 가져가셈
    for i in range(l1):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i]=-1

    #남에 거 빌리셈
    for i in range(l1):
        if lost[i]== -1: continue

        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            lost[i]=-1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            lost[i]=-1       

    for i in range(l1):
        if lost[i]!= -1:
            answer-=1

    return answer

print(solution(7,[2,3,4],[1,2,3,6]))