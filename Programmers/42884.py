#https://programmers.co.kr/learn/courses/30/lessons/42884
INF=int(1e9)

def solution(routes):
    answer = 0
    highway = []

    routes.sort()
    #print(routes)
    minOutTime=INF
    for inTime, outTime in routes:
        if minOutTime < inTime:
            answer+=1
            minOutTime=outTime
        elif minOutTime>outTime:
            minOutTime=outTime

    return answer+1