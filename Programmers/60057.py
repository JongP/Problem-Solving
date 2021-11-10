from typing import AnyStr

    
def solution(s):
    l=len(s)
    print(l)
    answer=l

    for i in range(1,l//2+1):
        tmp=0
        idx=0
        if i==2:
            print(1)
        while idx<l:

            repeatNum=1

            while idx+repeatNum*i+i-1<l:
                if s[idx:idx+i]!=s[idx+repeatNum*i:idx+repeatNum*i+i]:
                    break
                repeatNum+=1



            if repeatNum==1:
                if idx+i-1>=l:
                    tmp+=l-idx
                else:
                    tmp+=i
                idx+=i               
            else:
                idx=idx+repeatNum*i
                tmp+=len(str(repeatNum))+i
        


        #print(i,tmp)
        answer=min(answer,tmp)

    print(answer)
    return answer
    

solution("abcabcdede")