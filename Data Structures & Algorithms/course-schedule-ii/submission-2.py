class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for src, dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        output = []
        while q:
            n = q.popleft()
            output.append(n)
            for nei in adjList[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return output[::-1]
        