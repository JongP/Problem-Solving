class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        cnt=0
        answer=0
        while n:
            answer<<=1
            answer+=n%2
            cnt+=1
            n>>=1
            
        while cnt < 32:
            answer<<=1
            cnt+=1
        
        #print(answer)
        return(answer)

    def bestReverseBits(self, n):
        res    = 0
        for i in range(32):
            if n&1:#how to get mod 2 with bit manipulation
                res += 1 << (31-i)
            n >>= 1
        return res