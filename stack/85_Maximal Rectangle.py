class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res=0
        m=len(matrix)
        n=len(matrix[0])
        

        def findMaxHis(line):
            stk=[]
            res=0
            
            for i,v in enumerate(line):
                lowestIndex=i
                while stk and stk[-1][-1]>v:
                    lowestIndex,tmpH=stk.pop()
                    if res< (i-lowestIndex)*tmpH:
                        res=(i-lowestIndex)*tmpH
                stk.append([lowestIndex,v])

            while stk :
                idx,tmpH=stk.pop()
                if res< (len(line)-idx)*tmpH:
                    res=(len(line)-idx)*tmpH
                
            return res


        histos=[[0]*n for _ in range(m)]
        
        for j in range(n):
            tmp=0
            for i in range(m):
                if matrix[i][j]=="1":
                    if i>0:
                        histos[i][j]=histos[i-1][j]+1
                    else:
                        histos[i][j]=1
                else:
                    histos[i][j]=0
                    
                    
        for i in range(m):
            res= max(res,findMaxHis(histos[i]))
                    
        #print(histos)
        
        return res