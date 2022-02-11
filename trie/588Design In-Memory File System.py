class FileSystem:

    def __init__(self):
        self.dir={}
        self.keys=set(["C"])

    def ls(self, path: str) -> List[str]:
        if path=="/": return sorted(item for item in self.dir.keys()  if item!="C"  )
            
        path=path.split("/")
        trav=self.dir

        for i in range(1,len(path)):
            trav=trav[path[i]]
        
        if "C" in trav:
            return [path[-1]]
        return sorted(item for item in trav.keys()  if item!="C"  )

    def mkdir(self, path: str) -> None:
        path=path.split("/")
        trav=self.dir

        for i in range(1,len(path)):
            if path[i] not in trav:
                trav[path[i]]={}
            trav=trav[path[i]]
                
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        path=filePath.split("/")
        trav=self.dir

        for i in range(1,len(path)):
            if path[i] not in trav:
                trav[path[i]]={}
            trav=trav[path[i]]
            
        if "C" not in trav: trav["C"]=""
        trav["C"]+=content
        

    def readContentFromFile(self, filePath: str) -> str:
        path=filePath.split("/")
        trav=self.dir
        
        for i in range(1,len(path)):
            trav=trav[path[i]]
            
        return trav["C"]



#optimized solution
class FileSystem:

    def __init__(self):
        self.dir={"D":[]}
        self.keys=set(["C","D"])

    def ls(self, path: str) -> List[str]:
        if path=="/": return self.dir["D"] 
            
        path=path.split("/")
        trav=self.dir

        for i in range(1,len(path)):
            trav=trav[path[i]]
        
        if "C" in trav:
            return [path[-1]]
        
        return trav["D"]

    def mkdir(self, path: str) -> None:
        path=path.split("/")
        trav=self.dir

        for i in range(1,len(path)):
            if path[i] not in trav:
                trav[path[i]]={"D":[]}
                trav["D"].append(path[i])
                trav["D"].sort()
            trav=trav[path[i]]
                
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        path=filePath.split("/")
        trav=self.dir

        for i in range(1,len(path)):
            if path[i] not in trav:
                trav[path[i]]={"D":[]}
                trav["D"].append(path[i])
                trav["D"].sort()
            trav=trav[path[i]]
            
        if "C" not in trav: trav["C"]=""
        trav["C"]+=content
        

    def readContentFromFile(self, filePath: str) -> str:
        path=filePath.split("/")
        trav=self.dir
        
        for i in range(1,len(path)):
            trav=trav[path[i]]
            
        return trav["C"]


#https://leetcode.com/problems/design-in-memory-file-system/discuss/426854/python-scalable-trie-solution
from collections import defaultdict
class Node:
    def __init__(self):
        self.child=defaultdict(Node)
        self.content=""
        
class FileSystem(object):

    def __init__(self):
        self.root=Node()
        
    def find(self,path):#find and return node at path.
        curr=self.root
        if len(path)==1:
            return self.root
        for word in path.split("/")[1:]:
            curr=curr.child[word]
        return curr
        
    def ls(self, path):
        curr=self.find(path)
        if curr.content:#file path,return file name
            return [path.split('/')[-1]]
        return sorted(curr.child.keys())
		
    def mkdir(self, path):
        self.find(path)

    def addContentToFile(self, filePath, content):
        curr=self.find(filePath)
        curr.content+=content

    def readContentFromFile(self, filePath):
        curr=self.find(filePath)
        return curr.content