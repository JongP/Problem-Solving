class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[0]
        leftZero=0
        rightZero=0
        
        for i,v in enumerate(boxes):
            if v=="1": 
                ans[0]+=i
                rightZero+=1
        
        if boxes[0]=="1":
            leftZero=1
            rightZero-=1
        #print(ans)
        
        for i,v in enumerate(boxes[1:],start=1):
            #print(i,v)
            val=ans[-1]-rightZero+leftZero
            ans.append(val)
            
            if v=="1":
                leftZero+=1
                rightZero-=1
        
        return ans