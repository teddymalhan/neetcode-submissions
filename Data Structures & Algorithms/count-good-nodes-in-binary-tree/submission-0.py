# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node: Optional[TreeNode], maxTillNow: int):
            nonlocal good

            if not node:
                return

            if maxTillNow <= node.val:
                good += 1
            
            maxTillNow = max(maxTillNow, node.val)
            dfs(node.left, maxTillNow)
            dfs(node.right, maxTillNow)


        dfs(root, -math.inf)
        return good