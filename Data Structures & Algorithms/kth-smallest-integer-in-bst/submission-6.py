# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        # we want an inorder traversal here and basically just append those
        # values and return k-1 element

        def inorder(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return
            
            if node.left:
                inorder(node.left)
            
            res.append(node.val)

            if node.right:
                inorder(node.right)
            
        
        inorder(root)
        return res[k-1]
