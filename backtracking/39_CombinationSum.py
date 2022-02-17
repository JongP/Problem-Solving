class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]

        def helper(idx,cur,s):
            
            if s==target:
                self.res.append(cur[:])
                return
            
            if idx>=len(candidates) or s>target:
                return
            
            cur.append(candidates[idx])
            helper(idx,cur,s+candidates[idx])
            cur.pop()
            helper(idx+1,cur,s)
            
            
        
        helper(0,[],0)
        
        return self.res

#https://leetcode.com/problems/combination-sum/discuss/875365/JavaPython-Backtracking-Clean-and-Concise-Very-fast-~-2ms
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # sort to terminate early when target < 0
        
        def backtracking(i, target, path):
            if target == 0:
                ans.append(path)
                return
            if i == len(candidates) or target < candidates[i]:
                return
            backtracking(i, target - candidates[i], path + [candidates[i]]) # Choose ith candidate
            backtracking(i + 1, target, path) # Skip ith candidate
        
        ans = []
        backtracking(0, target, [])
        return ans

#https://leetcode.com/problems/combination-sum/discuss/751353/Python-92-Faster-97-Space
    def backtrack(self, candidates, target, r, s, i):        
        if s == target:
            self.res.append(r[:])
        
        for j in range(i, len(candidates)):
            c = candidates[j]
            if s + c > target: break
                
            # Place
            r.append(c)
            s += c
            # Search
            self.backtrack(candidates, target, r, s, j)
            
            # Backtrack
            r.pop()
            s -= c
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = list()
        self.backtrack(sorted(candidates), target, [], 0, 0)
        return self.res

#22-02-17
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        
        
        def helper(idx,path,target):
            if target==0:
                res.append(path.copy())
                return
            elif target<0 or idx==len(candidates):
                return
            
            
            l=target//candidates[idx]
            for i in range(l+1):
                helper(idx+1,path,target-i*candidates[idx])
                path.append(candidates[idx])
            
            for i in range(l+1): path.pop()     
            
                
            
        
        
        helper(0,[],target)
        
        
        return res

#solution
#O(N^(T/M+1))
#https://leetcode.com/problems/combination-sum/solution/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results