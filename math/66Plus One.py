class Solution:
    #O(n) O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        
        for i in range(len(digits)-1,-1,-1):
            carry,val=divmod(digits[i]+carry,10)
            
            digits[i]=val
        
            if carry==0:
                break

        if carry==1:
            digits.insert(0,1)
        
        
        return  digits

#https://leetcode.com/problems/plus-one/discuss/422298/python-solution-faster-than-97.02
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                break
            else:
                digits[idx] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits