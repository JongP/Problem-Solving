class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:return "Zero"
        firstDigits=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        secondDigits=["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        secondSp=["Ten","Eleven", "Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        HUD="Hundred"
        
        digits=["","Thousand","Million","Billion","Trillion"];digits.reverse()
        
        res=[]
        val=-1
        prevLen=0
        
        while num:
            
            addition=digits.pop()
            if addition: res.append(addition)
            
            
            prevLen=len(res)
            
            for i in range(3):
                prev=val
                num,val=divmod(num,10)

                if i==1:
                    if val==1:
                        if prev!=0:res.pop()
                        res.append(secondSp[prev])
                    elif val!=0:
                        res.append(secondDigits[val])
                elif val!=0:
                    if i==2: res.append(HUD)
                    res.append(firstDigits[val])
                    
                        
                
                if num==0: break
    
            if addition and prevLen==len(res): res.pop()
        
        
        return " ".join(reversed(res))