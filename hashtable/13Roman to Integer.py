class Solution:
    def romanToInt(self, s: str) -> int:
        
        Dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        subDict={"I":set(["V","X"]),"X":set(["L","C"]),"C":set(["D","M"])}
        
        res=0
        for i, c in enumerate(s):
            if c in subDict and i!=len(s)-1 and s[i+1] in subDict[c]:
                res-=Dict[c]
            else:
                res+=Dict[c]
            
            
        return res


#Roman numerals are usually written largest to smallest from left to right.
#https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]