class Solution:


    #revistied answer I made from my own solution and discussion
    def sumSubarrayMins(self, arr):
        MODULO=10**9+7
        ans=0
        stk=[]
        arr=[0]+arr+[0]

        for i,v in enumerate(arr):
            while stk and stk[-1][0]>v:
                tmpV,tmpI=stk.pop()
                ans=(ans+tmpV*(i-tmpI)*(tmpI-stk[-1][1]))%MODULO
            stk.append((v,i))

        return ans


    def sumSubarrayMins1(self, arr) :
        n,mod=len(A),10**9+7
        left,right=[0]*n,[0]*n
        s1,s2=[],[]

        for i in range(n):
            count=1
            while s1 and s1[-1][0]>arr[i]:
                count+=s1.pop()[1]
            left[i]=count
            s1.append((arr[i],count))
        
        for i in range(n)[::-1]:
            count=1
            while s2 and s2[-1][0]>arr[i]:
                count+=s2.pop()[1]
            right[i]=count
            s2.append((arr[i],count))
        
        return sum(a*l*r for a,l,r in zip(arr,left,right))%mod
        




sol=Solution()
print(sol.sumSubarrayMins([3,1,2,4]))