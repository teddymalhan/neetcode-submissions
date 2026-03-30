"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        def dfs(node: Optional[Node]) -> Optional[Node]:
            if not node:
                return None
            
            # since in python objects are hashable
            if node in oldToNew:
                return oldToNew[node]
            
            # copy value
            newNode = Node(node.val)
            oldToNew[node] = newNode

            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            

            return oldToNew[node]

        dfs(node)
        return oldToNew[node]