# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # deque of form node and print it or not
        q = deque([(root, 0)])
        res = []

        while q:
            length = len(q)
            for _ in range(length):
                n, depth = q.popleft()

                if depth == len(res):
                    res.append(n.val)

                if n.right: 
                    q.append((n.right, depth + 1))

                if n.left:
                    q.append((n.left, depth + 1))
                        
        return res
            
