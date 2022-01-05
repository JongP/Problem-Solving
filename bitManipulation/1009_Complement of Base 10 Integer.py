class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        cnt=0
        res=0
        while n:
            res+=((~n)&1)<<cnt
            cnt+=1
            n>>=1
            
        return res

#https://leetcode.com/problems/complement-of-base-10-integer/discuss/256740/JavaC%2B%2BPython-Find-111.....1111-greater-N
    def bitwiseComplement(self, N):
        X = 1
        while N > X: X = X * 2 + 1
        return X - N