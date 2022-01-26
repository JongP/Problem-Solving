#parametric programming..
class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        
        def helper(arr):
            if len(arr)<=1: return 1
            
            leftTree=[]
            rightTree=[]
            root=arr[0]
            for i in range(1,len(arr)):
                if arr[i]<root: leftTree.append(arr[i])
                else: rightTree.append(arr[i])
            
            res1=helper(leftTree)
            res2=helper(rightTree)
            
            
            
            
            return res1*res2*math.comb(len(leftTree)+len(rightTree),len(leftTree))%(10**9+7)
        
        return helper(nums)-1


#https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/discuss/819858/C%2B%2BPython.-Question-explained.-Then-detailed-solution.-Short.-Fast.-Readable.