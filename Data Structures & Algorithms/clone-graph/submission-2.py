"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # sanity check
        if not node:
            return None
            
        oTn = {}

        def dfs(node):
            if node in oTn:
                return oTn[node]
                
            clone = Node(node.val, None)
            oTn[node] = clone

            for neig in node.neighbors:
                clone.neighbors.append(dfs(neig))
            return clone
        return dfs(node)