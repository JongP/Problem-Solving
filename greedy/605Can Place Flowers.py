class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt=0
        
        #O(n), O(1)
        if n==0: return True
        if len(flowerbed)==1: return flowerbed[0]==0  or n==0
        
        #general casese
        prev=0
        for i in range(len(flowerbed)):
            nxt = flowerbed[i+1] if i<len(flowerbed)-1 else 0
            
            if prev==0 and flowerbed[i]==0 and nxt==0:
                flowerbed[i]=1
                cnt+=1
                if cnt>=n:
                    return True
            prev=flowerbed[i]
            
        

        return False

#check how to handle tail cases
#https://leetcode.com/problems/can-place-flowers/discuss/103890/Python-Straightforward-with-Explanation
    def canPlaceFlowers(self, A, N):
        for i, x in enumerate(A):
            if (not x and (i == 0 or A[i-1] == 0) 
                    and (i == len(A)-1 or A[i+1] == 0)):
                N -= 1
                A[i] = 1
        return N <= 0