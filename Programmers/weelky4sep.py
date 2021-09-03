import sys
input = sys.stdin.readline

def solution(table, languages, preference):
    answer = ''
    
    mytable ={}
    for row in table:
        tmp = row.split()
        mytable[tmp[0]]=tmp[1:]
    
    ansDict={}

    for industry in mytable:
        point =0

        for i in range(len(languages)):
            try:
                tmp_point=mytable[industry].index(languages[i])
                point+=(5-tmp_point)*preference[i]
            except:
                continue
        ansDict[industry]=point

    max=-1
    for ans in ansDict:
        if ansDict[ans]>=max:
            if ansDict[ans]==max and answer<ans: continue
            answer=ans 
            max=ansDict[ans]
    #print(ansDict)
    return answer

table =["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

print(solution(table,languages,preference))