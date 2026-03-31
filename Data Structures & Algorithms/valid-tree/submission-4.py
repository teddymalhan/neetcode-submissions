class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False
        
        adjList = [[] for _ in range(n)]
        indegree = [0]*n

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        # we have one end of the tree and should be able to traverse all of it
        start = 0
        for i in range(n):
            if indegree[i] == 1:
                start = i
                break
        
        visit = set()
        def dfs(i):
            nonlocal visit

            if i in visit:
                return False
            
            if len(visit) == n:
                return True

            visit.add(i)
            for nei in adjList[i]:
                if not dfs(nei):
                    return False
        
        return dfs(start)



        

