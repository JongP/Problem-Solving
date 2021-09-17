import sys
input = sys.stdin.readline

def solution(citations):
    citations.sort(reverse=True)
    answer=0
    l = len(citations)
    for i in range(l):
        if citations[i]>=(i+1) :
            if i<l-1 and citations[i+1]>(i+1):
                continue
            answer = i+1
            break


    return answer