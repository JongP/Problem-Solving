from sortedcontainers import SortedDict
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        l=len(arr)
        sortArr=SortedDict()
        sortArr[arr[-1]]=l-1
        
        oddSet=set([l-1])
        evenSet=set([l-1])

        
        for i in range(len(arr)-2,-1,-1):
            idx = sortArr.bisect_left(arr[i])
            
            #Oddset
            if arr[i] in sortArr: 
                if sortArr[arr[i]] in evenSet:
                    oddSet.add(i)
            elif idx!=len(sortArr) and sortArr.peekitem(idx)[1] in evenSet:
                    oddSet.add(i)
                
            
            #evenSet
            if arr[i] in sortArr:
                if sortArr[arr[i]] in oddSet:
                    evenSet.add(i)
            elif idx-1!=-1 and sortArr.peekitem(idx-1)[1] in oddSet:
                evenSet.add(i)
            
            
            #print(i,idx,sortArr,oddSet,evenSet)
            sortArr[arr[i]]=i
            
        #print(oddSet)
        return len(oddSet)
            
            
#https://leetcode.com/problems/odd-even-jump/discuss/1367042/Python-Sorted-Dict-and-Top-down-DP-Bottom-up-DP-Clean-and-Concise
from sortedcontainers import SortedDict
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        def findOddJump(sortedDict, x):
            if x in sortedDict: return sortedDict[x]
            idx = sortedDict.bisect_left(x)  # For example: [1, 4, 5], bisect_left(3) = 1 (because arr[1] = 4 > 3)
            if idx == len(sortedDict): return -1
            return sortedDict.peekitem(idx)[1]

        def findEvenJump(sortedDict, x):
            if x in sortedDict: return sortedDict[x]
            idx = sortedDict.bisect_left(x) - 1  # For example: [1, 4, 5], bisect_left(3)-1 = 0 (because arr[0] = 1 < 3)
            if idx == -1: return -1
            return sortedDict.peekitem(idx)[1]

        n = len(arr)
        oddJump, evenJump = [-1] * n, [-1] * n

        sortedDict = SortedDict()
        sortedDict[arr[-1]] = n - 1
        for i in range(n - 2, -1, -1):
            oddJump[i] = findOddJump(sortedDict, arr[i])
            evenJump[i] = findEvenJump(sortedDict, arr[i])
            sortedDict[arr[i]] = i

        @lru_cache(None)
        def dp(i, isOdd):
            if i == n - 1: return True
            if isOdd:
                if oddJump[i] == -1: return False
                return dp(oddJump[i], False)
            else:
                if evenJump[i] == -1: return False
                return dp(evenJump[i], True)
            
        return sum(1 for i in range(n) if dp(i, True))
        
        
        
        
            
        
        
        
#stack
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        v_i = [(v, i) for i, v in enumerate(arr)]
        svi = sorted(v_i) 
        oddnext = {}
        stack = []
        for v, i in svi:
            while stack and i > stack[-1][1]:
                pv, pi = stack.pop()
                oddnext[pi] = i
            stack.append((v, i))
        evennext = {}
        svi = sorted(v_i, key=lambda x: [-x[0], x[1]]) 
        stack = []
        for v, i in svi:
            while stack and i > stack[-1][1]:
                pv, pi = stack.pop()
                evennext[pi] = i
            stack.append((v, i))
        n = len(arr)
        oddReach = [False] * (n-1) + [True]
        evenReach = [False] * (n-1) + [True]
        for i in range(n-2, -1, -1):
            if i in oddnext:
                oddReach[i] = evenReach[oddnext[i]]
            if i in evennext:
                evenReach[i] = oddReach[evennext[i]]
        return collections.Counter(oddReach)[True]
            
        