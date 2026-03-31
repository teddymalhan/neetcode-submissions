# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
       

        def dfs(node):
            res = []
            q = deque([node])
            while q:
                qLen = len(q)
                level = []
                n = q.popleft()
                if n:
                    level.append(n)
                    q.append(n.left)
                    q.append(n.right)
                
                if level:
                    res.append(level)
            return res
        
        dfs(roto)
