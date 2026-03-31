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
                maximal_val = max(max_val, node.val) if max_val != math.inf else node.val
                left = dfs(node.left, min_val, maximal_val)

            if node.right:
                minimal_val = min(max_val, node.val) if max_val != -math.inf else node.val
                right = dfs(node.right, minimal_val, max_val)
            
            return left and right

        return dfs(root, -math.inf, math.inf)