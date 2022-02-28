class SnapshotArray:

    def __init__(self, length: int):
        self.l=length
        self.hashMap={}
        self.data=[[(-1,0)] for _ in range(length) ]
        self.sId=0
        

    def set(self, index: int, val: int) -> None:
        self.hashMap[index]=val
        
        if val==self.data[index][-1][1]:
            del self.hashMap[index]
        

    def snap(self) -> int:
        
        for i in self.hashMap:
            self.data[i].append((self.sId,self.hashMap[i]))
        
        self.sId+=1
        self.hashMap.clear()
        
        return self.sId-1
        

    def get(self, index: int, snap_id: int) -> int:
        #print(self.data)
        arr=self.data[index]
        
        #binary search
        le,ri,res=0,len(arr)-1,0 #miss len(arr)
        
        while le<=ri:
            mid=(le+ri)//2
            
            if arr[mid][0]>snap_id:
                ri=mid-1
            else:
                res=mid
                le=mid+1
                
        return arr[res][1] #miss(mid)
        

#https://leetcode.com/problems/snapshot-array/discuss/1335346/Python-HashMap-and-Binary-Search-Clean-and-Concise
class SnapshotArray:
    def __init__(self, length: int):
        self.map = defaultdict(list)
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        if self.map[index] and self.map[index][-1][0] == self.snapId:
            self.map[index][-1][1] = val
            return
        self.map[index].append([self.snapId, val])

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.map[index]
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if ans == -1: return 0
        return arr[ans][1]