#https://programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    people=deque(people)
    print(people)


    while people:
        bigNum = people.popleft()
        if people and people[-1]+bigNum<=limit:
            people.pop()
        answer+=1


    return answer

print(solution([50,50,80,70],100))