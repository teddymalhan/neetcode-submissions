class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # gross overestimate but now what can we do
        adjList = [[] for _ in range(len(edges) + 1)]
        indegree = [0]*(len(edges)+1)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 1:
                q.append(i)
            
        while q:
            n = q.popleft()
            indegree[n] = 0
            for nei in adjList[n]:
                if indegree[nei] > 0:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        for u, v in reversed(edges):
            if indegree[u] > 1 and indegree[v] > 1:
                return [u, v]
