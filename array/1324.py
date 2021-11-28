class Solution:
    def printVertically(self, s: str) -> List[str]:
        wList=s.split()
        l=len(wList)
        maxLen=max(list(map(len,wList)))
        
        print(wList,maxLen)
        ans=[]
        
        
        
        for i in range(maxLen):
            tmp=""
            
            for word in wList:
                if i>=len(word):
                    tmp+=" "
                    continue
                tmp+=word[i]
            ans.append(tmp.rstrip())
        
        
        return ans