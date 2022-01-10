#I made a constraint on this problem for myself not using the function int.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry="0"
        la=len(a)
        lb=len(b)
        
        res=""
        
        idx=-1
        while -1*idx<=la or -1*idx<=lb:
            #fetch
            na=a[idx] if -1*idx<=la else "0"
            nb=b[idx] if -1*idx<=lb else "0"
            
            
            #calculate
            cnt=[carry,na,nb].count("1")
            res+=str(cnt%2)
            carry="1" if cnt>=2 else "0"
            
            
            idx-=1
        
        if carry=="1":
            res+=carry

        return res[::-1]


#cheat
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a,2) + int(b,2)))[2:]



#https://leetcode.com/problems/add-binary/discuss/279879/Python-easy-to-understand
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]

