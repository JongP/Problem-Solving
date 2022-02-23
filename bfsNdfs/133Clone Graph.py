class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        hashMap={}
        
        
        def dfs(cur):
            if not cur: return None
            
            hashMap[cur]=Node(val=cur.val)
            
            
            for nxt in cur.neighbors:
                if nxt not in hashMap:
                    dfs(nxt)
                
                hashMap[cur].neighbors.append(hashMap[nxt])
                
        
        dfs(node)
        
        return hashMap[node]


#leetcode solution
class Solution(object):

    def __init__(self):
        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is original node and value being the clone node.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node