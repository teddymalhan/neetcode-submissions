class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False
        
        adjList = [[] for _ in range(n)]

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        visit = set()
        def dfs(i, parent):
            nonlocal visit

            if i in visit:
                return False
            
            if len(visit) == n:
                return True

            visit.add(i)
            for nei in adjList[i]:
                if nei == parent:
                    continue
                if not dfs(nei, i):
                    return False
            
            return True
        
        return bool(dfs(0, -1))