# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is just sum of two of the max depths of a tree
        def maxDepth(node):
            if not node:
                return 0

            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        diameter = maxDepth(root.left) + maxDepth(root.right)
        return diameter