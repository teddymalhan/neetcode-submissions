# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        def isSameTree(p: TreeNode, q: TreeNode):
            if not p and not q:
                return True
            
            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

            # if everything doesn't match return fasle
            return False

        if root and subRoot and isSameTree(root, subRoot):
            return True

        left = right = False
        if root.left:
            left = self.isSubtree(root.left, subRoot)
        if root.right:
            right = self.isSubtree(root.right, subRoot)
        return left or right  