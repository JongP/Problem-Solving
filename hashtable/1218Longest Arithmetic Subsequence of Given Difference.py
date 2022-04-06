class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        #O(n)
        hashMap={}
        
        for n in arr:
            if n-diff not in hashMap:
                hashMap[n]=1
                
            else:
                hashMap[n]=hashMap[n-diff]+1
            
                
        #print(hashMap)
        return max(hashMap.values())