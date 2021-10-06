from collections import deque

def solution(number, k):

    numbers=list(number)
    lenNum=len(numbers)
    queue=deque([])
    lenQue=0

    idx=0
    while idx<lenNum:
        while queue and number[idx]>queue[-1] and k!=0:
            queue.pop()
            k-=1
        queue.append(numbers[idx]) 

        idx+=1
    
    while(k!=0):
        queue.pop()
        k-=1

    return "".join(queue)


print(solution("125210",4))