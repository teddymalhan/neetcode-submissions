# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, -math.inf, +math.inf)])

        while q:
            n, left, right = q.popleft()
            if not (left < n.val < right):
                return False

            q.append((n.left, left, n.val))
            q.append((n.right, n.val, right))
        
        return True
            

