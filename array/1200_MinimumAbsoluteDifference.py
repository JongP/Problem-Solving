class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        dif=int(2e9)
        arr.sort()
        
        for i in range(len(arr)-1):
            tmp=arr[i+1]-arr[i]
            if tmp==dif:
                res.append([arr[i],arr[i+1]])
            elif tmp<dif:
                dif=tmp
                res=[[arr[i],arr[i+1]]]
        
        
        
        return res
        