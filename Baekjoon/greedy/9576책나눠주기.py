import heapq
import sys
input=sys.stdin.readline

ansL=[]

for _ in range(int(input())):
    n,m=map(int,input().rstrip().split())
    heap=[]
    res=0
    students=[tuple(map(int,input().rstrip().split())) for _ in range(m)]
    students.sort(reverse=True)
    
    for cur in range(1,n+1):
        while heap and heap[0]<cur:
            heapq.heappop(heap)

        while students and students[-1][0]<=cur:
            heapq.heappush(heap,students.pop()[1])
        if heap:
            heapq.heappop(heap)
            res+=1

    ansL.append(res)


[print(ans) for ans in ansL]


#https://www.acmicpc.net/source/28148226
import sys
input = sys.stdin.readline


def find_idx(a, b):
    for i in range(a, b+1):
        if not books[i]:
            return i
    return 0

for _ in range(int(input())):
    N, M = map(int, input().split(' '))
    data = []
    for _ in range(M):
        a, b = map(int, input().split(' '))
        data.append((a, b))

    # a, b가 작은 순서대로 정렬 -> a부터 b까지 중에서 가장 작은 번호로 반환 -> 그리디
    data = sorted(data, key=lambda x:(x[1], x[0])) # key point
    books = [False] * (N+1)
    for a, b in data:
        idx = find_idx(a, b)
        if idx > 0:
            books[idx] = True
    print(sum(books))