
class Solution:
    def minimumTime(self, s: str) -> int:
        """
        00100
        """
        l=len(s)
        rmCost=[0]*l
        rmCost[-1]=int(s[-1])
        for i in range(l-2,-1,-1):
            if s[i]=="1":
                rmCost[i]= min(l-i, 2+rmCost[i+1])
            else:
                rmCost[i]=rmCost[i+1]
                
        
        res=rmCost[0]
        
        for i in range(l):
            if s[i]=="1":
                res=min(res,(i+1) +(rmCost[i+1] if i!=l-1 else 0))
            
        return res

#https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/discuss/1748452/Python-Explanation-with-pictures.-Prefix-and-Suffix.
#get max cost and then, get max save
def minimumTime(self, A: str) -> int:
        n = len(A)
        if n == 1: return 1 if A == '1' else 0
        lft, rgt = [] * n, [] * n
        
        curr = 0
        for a in A:
            if a == '1':
                curr += 1
            else:
                curr -= 1
            lft.append(curr)
            
        curr = 0
        for a in A[::-1]:
            if a == '1':
                curr += 1
            else:
                curr -= 1
            rgt.append(curr)
        rgt.reverse()

        exp = 2 * A.count('1')   # MaximumCost, that is the cost of removing all cars with a cost of 2.
            
        lmax, curr = [lft[0]], lft[0]
        for i in range(1, n):
            curr = max(curr, lft[i])
            lmax.append(curr)
            
        rmax, curr = [rgt[-1]], rgt[-1]
        for i in range(n - 2, -1, -1):
            curr = max(curr, rgt[i])
            rmax.append(curr)            
        rmax.reverse()
        
        maxp = 0  # The maximum cost we can SAVE.
        for i in range(n - 1):
            maxp = max(maxp, max(0, lmax[i]) + max(0, rmax[i + 1]))

        return exp - maxp  # The overall cost is the MaximumCost - "the maximum cost we can save".