#43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        answer=0
        digit=1
        for i in range(len(num2)-1,-1,-1):
            mul=int(num2[i])
            
            digitTmp=1
            answerTmp=0
            for j in range(len(num1)-1,-1,-1):
                mulTmp=int(num1[j])
                answerTmp+=mul*mulTmp*digitTmp
                digitTmp*=10
                
            answer+=answerTmp*digit
                
            digit*=10
            
            
            
        return str(answer)