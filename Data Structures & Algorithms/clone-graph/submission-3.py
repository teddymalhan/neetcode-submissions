"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # eh? you visit a neighbour, add its value and check if it already exists and go down the stack
        # and backpropogate if you feel you went too deep
        oldToNew = {}
        def dfs(node: Node) -> Node:
            if node in oldToNew:
                return oldToNew[node]

            if not node:
                return

            newNode = Node(node.val)

            oldToNew[node] = newNode
            for neig in node.neighbors:
                newNode.neighbors.append(dfs(neig))
            return newNode
        
        return dfs(node)