class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        #1 brute force --> O(n^2)
        for c in s, c is start of substring
            #find  longest substring consisting of c until we have k changes
            AAAABA
            #chage c=s[i] to s[i+1]
            
        #2 kadane
        "A"
        "AB"
        "ABA"
        
        
        """
        l=len(s)
        chars=[0]*26
        
        def canMake(chars,k):
            maxVal=0
            total=0
            for n in chars:
                maxVal=max(maxVal,n)
                total+=n
                
            return total-maxVal<=k
        
        
        le=ri=0
        
        
        while ri<l:
            #shift right
            chars[ord(s[ri])-ord("A")]+=1
            
            #extend ri as much as possible
            if canMake(chars,k):
                while ri+1<l:
                    chars[ord(s[ri+1])-ord("A")]+=1
                    if not canMake(chars,k):
                        chars[ord(s[ri+1])-ord("A")]-=1
                        break
                    ri+=1
            
            
            
            #shift left
            chars[ord(s[le])-ord("A")]-=1
            
            le+=1
            ri+=1
            
        return ri-le+1


    def characterReplacement(self, s, k):
        maxf = res = 0
        count = collections.Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res - maxf < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res

#https://www.youtube.com/watch?v=gqXU1UyA8pk
    def characterReplacement(self, s, k):
        count={}
        res=0
        l=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res