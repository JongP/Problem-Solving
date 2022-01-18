#new concept
#NP problem
#https://gazelle-and-cs.tistory.com/64
#meet in the middle
#https://junghyunkwon3.wordpress.com/2016/01/18/knapsack-문제가-np인-이유/
#https://gazelle-and-cs.tistory.com/51
"""
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/discuss/1530354/Python-Solution-with-analogy
As the length of nums has upper bound n = 40, a brute force way of checking the
possible subsequnce sums will have time complexity 2 ** n. That is too large.
The idea here is to split the nums into two halves, each has length upper bound 20.
So getting all possible sums xs, ys for each part has time O(2 ** (n/2)).
In the algorithm, we sorted one of xs, ys, say ys, it takes O(2 **(n/2) * log(2 **(n/2)))
For each x in xs, we do binary search in ys to find nearest candidates (may need check twice, i.e,
left, right of the binary insertion index), the time is again O(2 **(n/2) * log(2 **(n/2)))
So overall time complexity is O(2 **(n/2) * log(2 *2(n/2))), i.e., O(n * 2 **(n/2)).
        
"""
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        #O(N*2^(N/2))
        n=len(nums)//2
        target=sum(nums)/2#check
        leftSums=[[] for _ in range(n+1)]
        rightSums=[[] for _ in range(n+1)]
        
        #meet in the middle
        def getCombSum(arr,s,e,path,pathN,res):
            if s>e:
                res[pathN].append(path)
                return
            getCombSum(arr,s+1,e,path,pathN,res)
            getCombSum(arr,s+1,e,path+arr[s],pathN+1,res)
            
            
        getCombSum(nums,0,n-1,0,0,leftSums)
        getCombSum(nums,n,2*n-1,0,0,rightSums)
        
        #sorting # O((2**N)*log(2**N))=O(N*2**(N/2)
        for i in range(n+1):
            leftSums[i].sort()
            rightSums[i].sort(reverse=True)
        
        
        res=math.inf
        #print(leftSums,rightSums)
        #counting w/ two pointers
        for i in range(n+1):
            leftSum=leftSums[i]
            rightSum=rightSums[n-i]
            idx1=idx2=0
            while idx1<len(leftSum) and idx2<len(rightSum):
                total=leftSum[idx1]+rightSum[idx2]
                if total>target:
                    idx2+=1
                else:
                    idx1+=1
                if res>abs(total-target)*2:
                    res=int(abs(total-target)*2)

        return res