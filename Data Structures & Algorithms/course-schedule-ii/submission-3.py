class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for src, dst in prerequisites:
            adjList[src].append(dst)
            indegree[dst] += 1

        print(f'adjList {adjList}')
        print(f'indegree {indegree}')
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        print(f'q {q}')

        output, coursesDone = [], 0
        while q:
            n = q.popleft()
            print(f'n {n}')
            coursesDone += 1
            output.append(n)
            for nei in adjList[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return output[::-1] if numCourses == coursesDone else []
        