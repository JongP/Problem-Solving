class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=triangle[0]
        
        for i in range(1,len(triangle)):
            preLine=triangle[i-1]
            curLine=triangle[i]
            orgLine=curLine.copy()
            curLine[0]=curLine[0]+preLine[0]            
            for idx,v in enumerate(preLine):
                curLine[idx]=min(curLine[idx],preLine[idx]+orgLine[idx])
                curLine[idx+1]=preLine[idx]+orgLine[idx+1]
            print(curLine)
        
        return min(triangle[-1])