import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    
    answer=-1
    clock=0
    while True:
        s1 = heapq.heappop(scoville)
        
        if s1>=K:
            answer=clock
            break
        
        if scoville:
            s2 = heapq.heappop(scoville)
        else:
            break
        
        heapq.heappush(scoville,s1+2*s2)
        clock+=1
    return answer
        
        
        
print(solution([1, 2, 3, 9, 10, 12],7))