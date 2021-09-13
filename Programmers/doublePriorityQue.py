import heapq

def solution(operations):
    maxHeap =[]
    minHeap = []
    num=0

    for operation in operations:
        operator, operand = operation.split()

        if operator == 'I':
            heapq.heappush(minHeap,int(operand))
            heapq.heappush(maxHeap,-1*int(operand))
            num+=1
        elif num<=0:
            continue
        else:
            if operand=="1":
                heapq.heappop(maxHeap)
            else:
                heapq.heappop(minHeap)
            num-=1
            if num==0:
                maxHeap=[]
                minHeap=[]
    
    if num==0:
        return [0,0]
    else:
        return [-1*maxHeap[0],minHeap[0]]

print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))