# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], min_val: int, max_val: int):
            if not node:
                return True
            
            if not (min_val < node.val < max_val):
                return False
            
            left, right = True, True
            if node.left:
                left = dfs(node.left, min_val, node.val)

            if node.right:
                right = dfs(node.right, node.val, max_val)
            
            return left and right

        return dfs(root, -math.inf, math.inf)