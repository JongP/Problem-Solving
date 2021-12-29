import sys
input=sys.stdin.readline
#map(int,input().rstrip().split())

class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def getHead(preorderList,inorderList):
    if len(preorderList)==0:
        return None
    elif len(preorderList)==1:
        return Node(val=preorderList[0])
    #elif len(preorderList)==2:


    headVal=preorderList[0]
    headInx=inorderList.index(headVal)

    #indexing is the most difficult part
    leftPre=preorderList[1:headInx+1]
    leftIn=inorderList[:headInx]

    rightPre=preorderList[headInx+1:]
    rightIn=inorderList[headInx+1:]
    #print(headVal,leftPre,leftIn,rightPre,rightIn)
    return Node(headVal,getHead(leftPre,leftIn),getHead(rightPre,rightIn))


def postorder(node,path):
    if not node:
        return
    
    postorder(node.left,path)
    postorder(node.right,path)

    path.append(node.val)

ansL=[]
for _ in range(int(input())):
    n=int(input())
    preorderList=list(map(int,input().rstrip().split()))
    inorderList=list(map(int,input().rstrip().split()))
    head=getHead(preorderList,inorderList)

    ans=[]
    postorder(head,ans)
    ansL.append(ans)



for ans in ansL:
    print(" ".join(map(str,ans)))