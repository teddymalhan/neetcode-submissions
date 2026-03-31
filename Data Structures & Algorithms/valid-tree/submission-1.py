class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # have to check if there are only limited edges
        if len(edges) > n - 1:
            return False

        # no cycles 
        indegree = [0]*n
        adjList = [[] for _ in range(n)]
        for src, dst in edges:
            indegree[dst] += 1
            adjList[src].append(dst)
        
        q = deque()
        for _ in range(n):
            if indegree[i] == 0:
                q.append(i)

        visited = 0
        while q:
            n = q.popleft()
            visited += 1
            for nei in adjList[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return visited == n