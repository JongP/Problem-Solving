class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def canSuc(array):
            if len(array)==1:
                #print(array[0])
                return abs(array[0]-24) < 1e-5
            

            l=len(array)
            
            for i in range(l-1):
                for j in range(i+1,l):
                    nArray=[value   for idx,value in enumerate(array) if idx!=i and idx!=j  ]
                    
                    op1,op2=array[i],array[j]
                    iters=[op1+op2,op1*op2,op1-op2,op2-op1]
                    if op1: iters.append(op2/op1)
                    if op2: iters.append(op1/op2)
                    
                    for newNum in iters:
                        nArray.append(newNum)
                        if canSuc(nArray): return True
                        nArray.pop()
                    

            return False
            
            
        return canSuc(cards)

#https://leetcode.com/problems/24-game/discuss/107669/Python-greater-90-ignore-brackets-solution-(O(1)-~-13824)
import itertools
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Ops = list(itertools.product([add,sub,mul,div], repeat=3))
        for ns in set(itertools.permutations(nums)):
            for ops in Ops:
                # (((W op X) op Y) op Z)
                result = ops[0](ns[0], ns[1])
                result = ops[1](result, ns[2])
                result = ops[2](result, ns[3])
                if 23.99 < result < 24.01:
                    return True

                # (Z op (Y op (W op X)))
                result = ops[0](ns[0], ns[1])
                result = ops[1](ns[2], result)
                result = ops[2](ns[3], result)
                if 23.99 < result < 24.01:
                    return True

                # ((W op X) op (Y op Z))
                result1 = ops[0](ns[0], ns[1])
                result2 = ops[1](ns[2], ns[3])
                result = ops[2](result1, result2)
                if 23.99 < result < 24.01:
                    return True
        return False

def add (a, b):
    return a+b
def sub (a, b):
    return a-b
def mul (a, b):
    return a*b
def div (a, b):
    if b == 0:
        return 0
    return a/float(b)