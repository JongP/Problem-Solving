class Solution:
    def findComplement(self, num: int) -> int:
        i=0
        res=0
        tmp=num
        while tmp:
            res |= ((~tmp&1))<<i
            #~(tmp&1))<<i  what is wrong with ths??
            i+=1
            tmp>>=1

        return res

#https://leetcode.com/problems/number-complement/discuss/96009/Simple-Python
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num