from collections import deque

def solution(cacheSize, cities):
    answer = 0


    l=len(cities)
    cache=deque([])


    if cacheSize==0:
        return 5*l

    lenQue=0
    for i in range(len(cities)):
        cityString=cities[i].lower()
        if cityString in cache:
            cache.remove(cityString)
            answer+=1
        else:
            if lenQue>=cacheSize:
                cache.popleft()
            else: 
                lenQue+=1
            answer+=5
        cache.append(cityString)


    print(answer)
    return answer


solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(1,["Jeju", "Pangyo", "Seoul", "Seoul"])
solution(7,["Jeju", "Pangyo", "Seoul", "Seoul"])