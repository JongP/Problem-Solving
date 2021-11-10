def solution(record):
    answer = []
    myDict={}
    idx=0
    for cmd in record:
        cmd = cmd.split()

        if cmd[0][0]=='E':
            if cmd[1] not in myDict:
                myDict[cmd[1]]=[cmd[2],[idx]]
            else:
                myDict[cmd[1]][0]=cmd[2]
                myDict[cmd[1]][1].append(idx)
            answer.append("님이 들어왔습니다.")    
            idx+=1
        elif cmd[0][0]=='L':
            myDict[cmd[1]][1].append(idx)
            answer.append("님이 나갔습니다.")
            idx+=1
        else:
            myDict[cmd[1]][0]=cmd[2]

    
    for key in myDict:
        name, indexes =myDict[key]
        for index in indexes:
            answer[index]=name+answer[index]


    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))