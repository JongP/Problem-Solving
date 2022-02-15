# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        res=[]
        que=collections.deque([(root,1)])
        
        while que:
            cur,val=que.popleft()
            res.append(str(cur.val)+":"+str(val))
            
            if cur.left:
                que.append((cur.left,val*2))
            if cur.right:
                que.append((cur.right,val*2+1))
                
            
            
        #print(",".join(res))
        return ",".join(res)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data=deque(map(lambda x: list(map(int,x.split(':'))),data.split(",")))
        for i in range(len(data)):
            data[i][0]=TreeNode(data[i][0])
        #print(data)
        
        ptr1=0
        ptr2=1
        
        while ptr2<len(data):
            val1,key1=data[ptr1][0],data[ptr1][1]
            val2,key2=data[ptr2][0],data[ptr2][1]
            
            if key1*2==key2:
                val1.left=val2
                ptr2+=1
            elif key1*2+1==key2:
                val1.right=val2
                ptr2+=1
                ptr1+=1
            else:
                ptr1+=1
            
        
        return data[0][0]
        

#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/212059/Python-solution
#dfs recursive
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root:
                res.append("None,")
                return 
            res.append(str(root.val)+",")
            dfs(root.left)
            dfs(root.right)
            
        res = []
        dfs(root)
        return "".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(q):
            if q[0] == "None":
                q.popleft()
                return
            root = TreeNode(q.popleft())
            l = helper(q)
            r = helper(q)
            root.left = l
            root.right = r
            return root
        
        lst = data.split(",")
        q = collections.deque(lst)
        return helper(q)

#recursive preorder --> DFS
#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/807180/Python-O(n)-by-DFS-w-Comment\
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # -----------------------------------
        def dfs(node):

            if not node:
                # base case:
                # empty node or leaf node
                dfs.path.append('X')

            else:
                # general case:
                # generate path preorder traversal
                dfs.path.append( str(node.val) )

                dfs( node.left )
                dfs( node.right )
        # -----------------------------------

        dfs.path = []
        dfs(node=root)
        return ' '.join(dfs.path)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        node_values = iter( data.split() )

        # --------------------------------
        def rebuild( node_values ):

            next_val = next( node_values )

            if next_val == 'X':
                # base case:
                # empty node or leaf node
                return None
            
            else:
                # general case:
                # rebuild with preorder path
                root = TreeNode(next_val)

                root.left = rebuild( node_values )
                root.right = rebuild( node_values )

                return root
        # --------------------------------
        return rebuild(node_values)

