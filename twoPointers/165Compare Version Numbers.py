class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1,version2= list(map(int,version1.split("."))), list(map(int,version2.split(".")))
        #print(len(version1),version2)
        
        idx=0
        mL=max(len(version1),len(version2))
        
        while idx <mL:
            v1=version1[idx] if idx<len(version1) else 0
            v2=version2[idx] if idx<len(version2) else 0
            # v1=idx<len(version1) and version1[idx] or 0
            # v2=idx<len(version2) and version2[idx] or 0
            
            if v1<v2:
                return -1
            elif v1>v2:
                return 1
            
            
            idx+=1

        return 0