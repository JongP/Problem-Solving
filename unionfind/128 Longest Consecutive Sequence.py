class Solution:
    
    def getParent(self,dic,num):
        if dic[num]==num:
            return num
        
        dic[num]=self.getParent(dic,dic[num])
        return dic[num]
        
    
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        res=0
        
        for num in nums:
            if num-1 in dic:
                dic[num]=dic[num-1]
            else:
                dic[num]=num
                
            if num+1 in dic:
                dic[num+1]=dic[num]
            
        for num in nums:
            p=self.getParent(dic,num)
            #print(num,p)
            if res<num-p+1:
                res=num-p+1
                
        
        
        return res

#union find
#https://leetcode.com/problems/longest-consecutive-sequence/discuss/474127/Union-Find-solution-or-python
class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        # remove the duplicate if any
        nums = set(nums)
        
        group, size = {}, {}
        
        for n in nums:
            group[n] = n
            size[n] = 1
            
        def find(a):
            if group[a] != a:
                group[a] = find(group[a])
            return group[a]
            
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                group[rb] = ra
                size[ra] += size[rb]
        
        for n in nums:
            if n - 1 in nums:
                union(n, n-1)
            #if n + 1 in nums:
            #    union(n, n+1)
        
        return max(size.values())

#hash map
#https://leetcode.com/problems/longest-consecutive-sequence/discuss/41212/Python-solution-in-HashMap-with-explanation
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unions = {};
        maxlen = 0;
        for n in nums:
            if unions.has_key(n): # duplicate n, skip
                continue;
            start = end = n;
            if unions.has_key(n+1): # update end if has bigger neighbouring section
                end = unions[n+1][1];
            if unions.has_key(n-1): # update start if has smaller neighbouring section
                start = unions[n-1][0];
            unions[start] = unions[end] = unions[n]=(start,end);
            maxlen = max(end-start+1, maxlen);
        return maxlen;