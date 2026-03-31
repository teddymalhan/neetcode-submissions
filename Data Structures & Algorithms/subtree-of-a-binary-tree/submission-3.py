# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p is None and q is None:
                return True
            
            if p and q and p.val == q.val:
                return bool(isSameTree(p.left, q.left) and isSameTree(p.right, q.right))
            
            return False
        
        if root is None and subRoot is None:
            return True
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)