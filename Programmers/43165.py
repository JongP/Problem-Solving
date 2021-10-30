#https://programmers.co.kr/learn/courses/30/lessons/43165
def DFS(i,sumA,l,target,numbers):
    if(i==l-1):

        if(sumA==target):
            global answer
            answer+=1
        return
    
    DFS(i+1,sumA+numbers[i+1],l,target,numbers)
    DFS(i+1,sumA+numbers[i+1]*(-1),l,target,numbers)
        
    
def solution(numbers, target):
    global answer 
    answer= 0
    
    l = len(numbers)
    
    DFS(0,numbers[0],l,target,numbers)
    DFS(0,numbers[0]*(-1),l,target,numbers)
        
        
    
    return answer

print(solution([1,1,1,1,1],3));