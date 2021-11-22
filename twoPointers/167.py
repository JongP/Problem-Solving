#167. Two Sum II - Input Array Is Sorted
#본 거
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        le=0
        ri=len(numbers)-1
        
        while le<ri:
            sumNum=numbers[le]+numbers[ri]
            if sumNum<target:
                le+=1
            elif sumNum>target:
                ri-=1
            else:
                break
                
        return [le+1,ri+1]