#Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer=0
        for num in bin(x^y):
            if num=='1':
                answer+=1
        return answer