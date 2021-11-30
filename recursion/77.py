from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [ list(x)  for x in combinations([i+1 for i in range(n)],k) ]
#https://leetcode.com/problems/combinations/discuss/170834/Python-solution
    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        elif k == 1:
            return [[i] for i in range(1,n+1)]
        res = []
        for tail in range(n,k-1,-1):
            tmp = self.combine(tail-1, k-1)
            for i in range(len(tmp)):
                tmp[i].append(tail)
            res += tmp
        return res
#https://leetcode.com/problems/combinations/discuss/844096/Backtracking-cheatsheet-%2B-simple-solution
    def combine2(self, n, k): 
        sol=[]
        def backtrack(remain,comb,nex):
			# solution found
            if remain==0:
                sol.append(comb.copy())
            else:
				# iterate through all possible candidates
                for i in range(nex,n+1):
					# add candidate
                    comb.append(i)
					#backtrack
                    backtrack(remain-1,comb,i+1)
					# remove candidate
                    comb.pop()
            
        backtrack(k,[],1)
        return sol