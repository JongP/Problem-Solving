class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #we need to implement a tree-time counter(base 3) that if a bit appears three time ,it will be zero.
        #curent  income  ouput
        # ab      c/c       ab/ab
        # 00      1/0       01/00
        # 01      1/0       10/01
        # 10      1/0       00/10
        # a=~abc+a~b~c;
        # b=~a~bc+~ab~c;
        
        a =0
        b = 0
        
        for c in nums:
            ta=(~a&b&c)| (a&~b&~c)
            b=~a&~b&c|~a&b&~c
            a=ta
            
        return a|b