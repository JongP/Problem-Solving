class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #prefixSum,SurfixSum
        prefixSum,surfixSum = self.getSum(cardPoints)
        #0~k
        #print(prefixSum,surfixSum)
        res=max(surfixSum[-k],prefixSum[k-1])
        
        for i in range(k-1):
            res=max(res,prefixSum[i]+surfixSum[-(k-i-1)])
            
            
        return res
            
            
            
            
    
    def getSum(self,array):
        l=len(array)
        p,s=[0]*l,[0]*l
        p[0]=array[0]
        s[-1]=array[-1]
        
        for i in range(1,l):
            j=l-i-1
            
            p[i]=p[i-1]+array[i]
            s[j]=s[j+1]+array[j]
            
        
        return p,s
        
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0
        
        for i, v in enumerate(cardPoints):
            curr += v
            if i - j + 1 > size:
                curr -= cardPoints[j]
                j += 1
            if i - j + 1 == size:    
                minSubArraySum = min(minSubArraySum, curr)
				
        return sum(cardPoints) - minSubArraySum