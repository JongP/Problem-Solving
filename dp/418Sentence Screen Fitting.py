class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """
        
        sIdx=0
        cIdx=0
        
        for every single row:
            col=0
            #1 sIdx~nextSdx #O(log n )
            #surfix Sum of total length
            # update cIdx ,col
            
            #if space is left
                #2 0~ end of sentence #O(1)
                # cal how many whole line can be placed in left columns(spaces)
                update col

                #3 0 ~ sIdx #O(n-->log n )
                # figure out how many words (not whole line possibly) can be palced in left spaces:
                # update sIdx
            
            
            sIdx+1
            
        
        
        """
        
        
        #1 cal prefixSum
        prefix=[0]*(len(sentence)+1)
        for i,v in enumerate(sentence):
            prefix[i+1]=prefix[i]+len(v)
        
        
        
        def calNextSIdx(sIdx,leftSpace):
            res=(-1,0)
            
            le,ri=sIdx,len(sentence)-1
            
            while le<=ri:
                mid=(le+ri)//2
                
                spaceConsumed = prefix[mid+1]-prefix[sIdx] + (mid-sIdx)
                if spaceConsumed<=leftSpace:
                    res=(mid,leftSpace-spaceConsumed)
                    le=mid+1
                else:
                    ri=mid-1
            
            return res
        
        
        count=0
        sIdx=0
        fullCost=prefix[-1]+len(sentence)-1
        
        """
        sIdx=0
            full sentence filled
            not
        sIdx!=0
        
        """
        dp={}
        for i in range(rows):
            if sIdx in dp:
                count+=dp[sIdx][1]
                sIdx=dp[sIdx][0]
                continue
                
                
            orginal=sIdx
            tmp=0
            
            leftSpace=cols
            #1 part 1
            nextIdx,leftSpace = calNextSIdx(sIdx,leftSpace)
            
            #print(nextIdx)
            
            if nextIdx!=-1:
                    sIdx=(nextIdx+1)%len(sentence)
            
            if nextIdx==len(sentence)-1:
                tmp+=1
            else:
                dp[orginal]=(sIdx,tmp)
                count+=tmp
                continue
                
            if leftSpace<=0:
                dp[orginal]=(sIdx,tmp)
                count+=tmp
                continue
                
            #2 full sentences
            mul,leftSpace = divmod(leftSpace,fullCost+1)
             #abc"______"
            
            tmp+=mul
            if leftSpace<=1:
                dp[orginal]=(sIdx,tmp)
                count+=tmp
                continue
            
            nextIdx,leftSpace = calNextSIdx(0,leftSpace-1)
            
            if nextIdx!=-1:
                sIdx=(nextIdx+1)%len(sentence)
            
            dp[orginal]=(sIdx,tmp)
            count+=tmp
            
            
        return count
            
            
            
            
#https://leetcode.com/problems/sentence-screen-fitting/discuss/1353833/Python-From-Brute-Force-to-DP-Easy-to-understand-Clean-and-Concise            
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)

        @lru_cache(None)
        def dp(i):  # Return (nextIndex, times) if the word at ith is the beginning of the row
            c = 0
            times = 0
            while c + len(sentence[i]) <= cols:
                c += len(sentence[i]) + 1
                i += 1
                if i == n:
                    times += 1
                    i = 0
            return i, times

        ans = 0
        wordIdx = 0
        for _ in range(rows):
            ans += dp(wordIdx)[1]
            wordIdx = dp(wordIdx)[0]
        return ans