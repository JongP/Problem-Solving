class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnts=[0]*26
        res=[]
        
        for c in s:
            cnts[ord(c)-ord('a')]+=1

                
                        
        def helper(res,prev,repeat):
            
            idx=25
            while idx>=0:
                if cnts[idx]>0 and not (idx==prev and repeat==repeatLimit):
                    break
                idx-=1
            
            if idx!=-1:
                res.append(chr(idx+ord('a')))
                cnts[idx]-=1
                repeat= repeat+1 if idx==prev else 1
                helper(res,idx,repeat)
            
            
            return
        
        
        helper(res,-1,0)
        
        
        
        return "".join(res)


#https://leetcode.com/problems/construct-string-with-repeat-limit/discuss/1784718/C%2B%2B-Greedy-%2B-Counting-O(N)-Time-O(1)-space
# Priority:
# 1. Lexographic maximum
# 2. maximum length 

# O(n) , if we do not sort and chcek all chars from 'z to a' in backward direction 

class Solution:
    def repeatLimitedString(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        p =list(d.keys())
        p.sort(reverse = True)
        for i in range(len(p)):
            while d[p[i]]>0:
                need = min(k , d[p[i]])
                d[p[i]]-=need
                temp = p[i]*need
                ans = ans + temp
                
                
                if d[p[i]]>0:
                    f = 0         # flag for next less charcter
                    for j in range(i+1, len(p)):
                        if d[p[j]]>0:
                            ans = ans + p[j]
                            d[p[j]]-=1
                            f = 1
                            break
                    if not f:  # if we do not get any less char to add , we need to stop here only!
                        return ans
              
        return ans
