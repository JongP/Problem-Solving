from math import lcm
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MODULO=10**9+7
        LCM=lcm(a,b)
        
        le=min(a,b)
        ri=min(a,b)*n

        
        while le<ri:
            mid=(le+ri)//2
            
            numMag=mid//a+mid//b-mid//LCM
            
            if numMag>n:
                ri=mid-1
            elif numMag<n:
                le=mid+1
            else:
                ri=mid
                
        return le%MODULO


"""
How many magic numbers <= x ?
By inclusion exclusion principle, we have:
x / A + x / B - x / lcm
"""
#solved with hint
#https://leetcode.com/problems/nth-magical-number/discuss/154613/C%2B%2BJavaPython-Binary-Search
#nth number <--> there are n magical number smaller than x
#don't forget to apply MODULO!!