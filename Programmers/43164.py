#https://programmers.co.kr/learn/courses/30/lessons/43164

def DFS(nextCity,depth):
    global answer,answerFlag,tmp_answer, graph,lenCity,l
    #print(tmp_answer)
    if(depth==l+1):
        #print(tmp_answer)
        #print(answer,tmp_answer)
        if(len(tmp_answer)==l+1 and answer>tmp_answer):
            answer=tmp_answer[:]  #without [:], we have severe problem, cuz list is reference data varialbe
            #print(answer)
        return



    #also consider in case you can't make move anymore
    if nextCity not in graph:
        return
    fixed_lit=graph[nextCity][:]
    if(len(fixed_lit)==0):
        return

    for city in fixed_lit:
        graph[nextCity].remove(city)
        tmp_answer.append(city)
        DFS(city,depth+1)
        tmp_answer.pop()
        graph[nextCity].append(city)

    return


def solution(tickets):
    global answer,answerFlag,tmp_answer, graph,lenCity,l
    answer = []
    answerFlag=False
    graph={}
    l=0
    cities=set()
    lenCity=0
    for a,b in tickets:
        l+=1
        if a not in cities:
            cities.add(a)
            lenCity+=1
        if b not in cities:
            cities.add(b)
            lenCity+=1
    
        if a not in graph:
            graph[a]=[b] #중복 없다 가정하고
        else:
            graph[a].append(b)

    #print(graph)
    for _ in range(l+1):
        answer.append("ZZZ")

    
    tmp_answer=["ICN"]
    DFS("ICN",1)
    print(answer)
    return answer

solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]])