# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
            return False
        
        if not root and subRoot:
            return True
        
        if root and subRoot and isSameTree(root, subRoot):
            return True
        
        left, right = False, False
        if root.left:
            left = self.isSubtree(root.left, subRoot)
        
        if root.right:
            right = self.isSubtree(root.right, subRoot)
        
        return left or right
