class Solution:
    #O(n) O(1)
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3: return False
        
        idx=0
        flag=False
        while idx<len(arr)-1 and arr[idx]<arr[idx+1]: 
            idx+=1
            flag=True
        if not flag: return False
            
        flag=False
        while idx<len(arr)-1:
            if arr[idx]<=arr[idx+1]: return False
            idx+=1
            flag=True
        if not flag: return False
        
        
        return True

#you can read an array in opposite direction!!
#https://leetcode.com/problems/valid-mountain-array/discuss/194900/C%2B%2BJavaPython-Climb-Mountain
    def validMountainArray(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1