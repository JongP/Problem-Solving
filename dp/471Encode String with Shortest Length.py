class Solution:
    #unsolved
    def encode(self, s, memo={}):
        if s not in memo:
            n = len(s)
            i = (s + s).find(s, 1)
            one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s
            multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)]
            memo[s] = min([s, one] + multi, key=len)
        return memo[s]


class Solution:
    def encode(self, s: str) -> str:
   
        # abc abc abc +bdsfhweuih 
        #3[abc]
        #a
        
        l=len(s)
        
        @functools.lru_cache()
        def backtracking(idx,idx2):
            if idx==idx2+1: return ""

            #not compression
            candidateWord=s[idx]+backtracking(idx+1,idx2)
            candidateLen=len(candidateWord)
            
            #in case compression
            le=ri=idx
            
        
            while ri<idx2+1:
                
                pattern=s[le:ri+1]
                nRi=ri
                
                cnt=1
                #if le==0 and ri==3:
                    #print(pattern,s[nRi+1:nRi+ri-le+2],nRi+ri-le+1 ,l )
                while nRi+ri-le+1 <idx2+1 and pattern==s[nRi+1:nRi+ri-le+2]:
                    nRi+=ri-le+1
                    cnt+=1
                    
                    
                if nRi-le+1> ri-le+4:
                    curWord=backtracking(le,ri)
                    leftWord=backtracking(nRi+1,idx2)
                    
                    if candidateLen>len(curWord)+2+len(str(cnt))+len(leftWord):
                        candidateLen=len(curWord)+2+len(str(cnt))+len(leftWord)
                        candidateWord= str(cnt)+"["+ curWord +"]" +leftWord
            
                ri+=1
                
            return candidateWord

        return backtracking(0,l-1)
        
        