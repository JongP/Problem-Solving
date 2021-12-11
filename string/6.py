class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans=""
        l=len(s)
        if l==1 or numRows==1:
            return s
        
        P=(numRows-1)*2
        
        for sIdx in range(numRows):
            
            for i in range(sIdx,l,P):
                ans+=s[i]
                if i%(numRows-1)!=0 and i+P-2*sIdx<l:
                    ans+=s[i+P-2*sIdx]
            #print(sIdx,ans)
        
        
        return ans
#https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        # This is a vague sentence for python beginers
        L = [''] * numRows

        index, step = 0, 1

        for x in s:
            L[index] += x
            #@1 start #
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)