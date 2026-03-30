class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
        
        visited = set()
        def dfs(i):
            visited.add(i)
            for nei in adjList[i]:
                if nei not in visited:
                    dfs(nei)

        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components