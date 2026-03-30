# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maximum = 0
        self.depth = {}

    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        if node in self.depth:
            return self.depth[node]
        
        self.depth[node] =  1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        return self.depth[node]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maximum = max(self.maximum, self.maxDepth(root.left) + self.maxDepth(root.right))
        if root.left:
            self.diameterOfBinaryTree(root.left)
        if root.right:
            self.diameterOfBinaryTree(root.right)
    
        return self.maximum