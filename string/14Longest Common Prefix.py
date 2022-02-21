class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=[]
        idx=0
        
        while True:
            stopFlag=False
            
            for word in strs:
                if idx==len(word) or word[idx]!=strs[0][idx]:
                    stopFlag=True
                    break
            
            if stopFlag: break
                
            res.append(strs[0][idx])
            idx+=1
        
        
        
        return "".join(res)

#https://leetcode.com/problems/longest-common-prefix/discuss/6918/Short-Python-Solution
    def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            if not strs:
                return ""
            shortest = min(strs,key=len)
            for i, ch in enumerate(shortest):
                for other in strs:
                    if other[i] != ch:
                        return shortest[:i]
            return shortest 