class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res=[]
        
        start,end=intervals[0]
        
        for i in range(1,len(intervals)):
            cS,cE=intervals[i]
            
            if cS<=end:
                end=max(cE,end)
            else:
                res.append([start,end])
                start,end=cS,cE
        
        res.append([start,end])
        
        
        return res
    
    
"""In python2, because range(n) will create a list with n element, so the space complexity is O(n).

In python3, range(n) will return an iterator(without creating the whole n-length list), so the space complexity is O(1)."""

#example solution
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        stack = []
        for i in intervals:
            if stack:
                #compare stack[-1] and i
                if stack[-1][1]>=i[0]:
                    new_value = [stack[-1][0],max(i[1],stack[-1][1])]
                    stack.pop()
                    stack.append(new_value)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return stack
#https://leetcode.com/problems/merge-intervals/discuss/350272/Python3-Sort-O(Nlog(N))
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda x: x[0])
        merged =[]
        for i in intervals:
			# if the list of merged intervals is empty 
			# or if the current interval does not overlap with the previous,
			# simply append it.
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
			# otherwise, there is overlap,
			#so we merge the current and previous intervals.
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged