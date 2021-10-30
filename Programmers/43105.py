def solution(triangle):
    answer = 0
    
    prev_line=[triangle[0][0]]
    
    for i in range(1,len(triangle)):

        
        tmp = [0]*(i+1)
        
        for j in range(len(prev_line)):
            tmp[j]=max(prev_line[j]+triangle[i][j],tmp[j])
            tmp[j+1]=max(prev_line[j]+triangle[i][j+1],tmp[j+1])
        #print(tmp)
        prev_line=tmp
        

    return max(prev_line)