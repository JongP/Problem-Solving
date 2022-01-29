#hint on related topic "trie"

class Trie:
    def __init__(self,maxLen):
        self.trie={}
        self.maxLen=maxLen
    
    def add(self,item: str):
        trav=self.trie
        
        for ch in item:
            if ch not in trav:
                trav[ch]={}
            trav=trav[ch]
            
        trav["*"]={}
        
    def getMax(self,num: str):
        res=0
        n=len(num)
        trav=self.trie
        #go maxLen-n step
        for _ in range(self.maxLen-n):
            if "1" in trav:
                trav=trav["1"]
                res<<=1
                res+=1
            else:
                trav=trav["0"]
                res<<=1
        
        
        #go n step
        for i in range(n):
            #go to "0"
            if (num[i]=="1" and "0" in trav) or (num[i]=="0" and "1" in trav):
                trav=trav["0" if num[i]=="1" else "1"]
                res<<=1
                res+=1
            else:
                trav=trav["1" if num[i]=="1" else "0"]
                res<<=1
        
        return res


class Solution:
    
    
    def toBin(self,nums: List[int]) -> tuple:
        maxLen=0
        res=[]
        
        for num in nums:
            res.append(bin(num)[2:])
            if maxLen<len(res[-1]): maxLen=len(res[-1])
            
        return res,maxLen
    
    
    def buildTrie(self,nums,maxLen):
        trie=Trie(maxLen)
        for num in nums:
            if len(num)==maxLen:
                trie.add(num)
                
        return trie
    
    
    def getMax(self,trie,nums) -> int :
        res=0
        
        for num in nums:
            tmp=trie.getMax(num)
            #print(num,tmp)
            if tmp>res: res=tmp
        
        return res
    
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        #O(n)
        
        #input processing
        nums,maxLen = self.toBin(nums)
        #print(nums,maxLen)
        trie = self.buildTrie(nums,maxLen)
        #print(trie.trie)
        
        
        #run through array + find max
        return self.getMax(trie,nums)


#https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/1345905/C%2B%2BPython-Trie-Solution-Clean-and-Concise-O(32N)
class TrieNode:
    def __init__(self):
        self.child = {}
        self.go = 0  # Number of elements goes through this node
    def increase(self, number):
        cur = self
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child: cur.child[bit] = TrieNode()
            cur = cur.child[bit]
            cur.go += 1
    def findMax(self, number):
        cur, ans = self, 0
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child and cur.child[1-bit].go > 0:
                cur = cur.child[1 - bit]
                ans |= (1 << i)
            else:
                cur = cur.child[bit]
        return ans
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trieNode = TrieNode()
        for x in nums:
            trieNode.increase(x)
            
        ans = 0
        for x in nums:
            ans = max(ans, trieNode.findMax(x))
        return ans


#https://www.geeksforgeeks.org/maximum-xor-of-two-numbers-in-an-array/
# Python3 implementation of the above approach
 
# Function to return the
# maximum xor
def max_xor( arr , n):
     
    maxx = 0
    mask = 0;
 
    se = set()
     
    for i in range(30, -1, -1):
         
        # set the i'th bit in mask
        # like 100000, 110000, 111000..
        mask |= (1 << i)
        newMaxx = maxx | (1 << i)
     
        for i in range(n):
             
            # Just keep the prefix till
            # i'th bit neglecting all
            # the bit's after i'th bit
            se.add(arr[i] & mask)
 
        for prefix in se:
             
            # find two pair in set
            # such that a^b = newMaxx
            # which is the highest
            # possible bit can be obtained
            if (newMaxx ^ prefix) in se:
                maxx = newMaxx
                break
                 
        # clear the set for next
        # iteration
        se.clear()
    return maxx
 
# Driver Code
arr = [ 25, 10, 2, 8, 5, 3 ]
n = len(arr)
print(max_xor(arr, n))
 
# This code is contributed by ANKITKUMAR34

#example solution
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        l = len(bin(max(nums))) - 2 
        """get the len of max number in nums in binary. -2 for '0b'
        if we want to look at the left most bit only, we just need 
        to to to right as much as the len of that number -> so we start from l - 1
        we will be working in the right most side to slowly build the output which 
        is from the left to right"""
        
        max_xor = 0
        for i in range(l-1, -1, -1):
            # what ever we make for max_xor we should
            #move it to left to move on to the next bit
            max_xor <<= 1
            current_xor = max_xor | 1 
            #we want to reach for the highest 
            #possible for this bit which is 1 but next time is 11 and so forth
            prefixes = {x >> i for x in nums} 
            # so if we have 5 bits in each num 
            #and we shift 4 times, we get the left most bit, 
            #next time the left most two bits
            max_xor |= any(current_xor^p in prefixes for p in prefixes) 
            # looking for a p1^p2 = current_xor (that gives 1). 
            #instead for each p we can look for its complement which is current_xor ^ p in the prefixes
        return max_xor