class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for src, dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        coursesDone = 0
        while q:
            n = q.popleft()
            coursesDone += 1
            for nei in adjList[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return coursesDone == numCourses