class Solution:

    #stk solution  17% 93%
    #first mistake w/o setting tmpD which implies that digits can more than 1-digit number
    
    #clean solution
    def search(self, nums: List[int], target: int) -> int:
        l=len(nums)
        t=target
        
        if l==1:
            return 0 if nums[0]==target else -1
        
        le=0
        ri=l-1
        
        while le<=ri:
            mid=(le+ri)//2
            if t<nums[mid] and t<nums[le] and nums[mid]>=nums[le]:
                le=mid+1
            elif t>nums[mid] and t>nums[ri] and nums[mid]<nums[ri] :
                ri=mid-1
            elif t<nums[mid]:
                ri=mid-1
            elif t>nums[mid]:
                le=mid+1
            else:
                return mid
            
            
        return -1
    def decodeString(self, s: str) -> str:
        s="1["+s+"]"#we dont need this actually
        stk=[]
        tmp=""
        tmpD=""
        for char in s:
            
            if char.isdigit():
                tmpD+=char

            elif char=="[":
                stk.append((int(tmpD),tmp))
                tmpD=""
                tmp=""
            elif char=="]":
                digit,chars=stk.pop()
                tmp=chars+tmp*digit
            elif char.isalpha():
                tmp+=char        
        
        
        
        return tmp



    #recursion solution/ 83%, 19%
    def decodeString(self, s: str) -> str:
        s="1["+s+"]"
        stk=[]
        tmp=""
        tmpD=""

        def helper(s,idx):
            tmp=""
            tmpD=""
            i=idx
            while i<len(s):
                if s[i].isdigit():
                    tmpD+=s[i]
                elif s[i]=="[":
                    chars,tmpI=helper(s,i+1)
                    tmp+=chars*int(tmpD)
                    tmpD=""
                    i=tmpI+1
                    continue
                elif s[i]=="]":
                    return tmp,i
                elif s[i].isalpha():
                    tmp+=s[i]   
                i+=1
            return tmp
       
        
        return helper(s,0)

#solution in discussion
#https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString