import heapq
import sys
input = sys.stdin.readline

n= int(input())
smallHeap=[]
smallHeapLen=0
largeHeap=[]
largeHeapLen=0

ansList=[]

#initialization
mid = int(input())
ansList.append(mid)
smallHeap.append(-1*mid)
smallHeapLen+=1

for _ in range(n-1):
    new_num = int(input())

    #adding new number in heap
    if new_num> -1*smallHeap[0]:
        heapq.heappush(largeHeap,new_num)
        largeHeapLen+=1
    else:
        heapq.heappush(smallHeap,-1*new_num)
        smallHeapLen+=1

    #calibrating heap and finding new heap
    if largeHeapLen>smallHeapLen:
        heapq.heappush(smallHeap,-1*heapq.heappop(largeHeap))
        largeHeapLen-=1
        smallHeapLen+=1
    elif largeHeapLen+1<smallHeapLen:
        heapq.heappush(largeHeap,-1*heapq.heappop(smallHeap))
        largeHeapLen+=1
        smallHeapLen-=1

    ansList.append(smallHeap[0]*-1)
for i in ansList:
    print(i)