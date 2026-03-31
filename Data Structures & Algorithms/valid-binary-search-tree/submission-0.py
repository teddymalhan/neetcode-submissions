# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([])
        q.append(root)

        while q:
            n = q.popleft()
            q.append(n.left)
            q.append(n.right)
            if n.left and n.val < n.left.val:
                return False
            if n.right and n.val > n.right.val:
                return False
        
        return True