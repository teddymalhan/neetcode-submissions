class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        indegree = [0]*n
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)
            indegree[src] += 1
            indegree[dst] += 1
        
        print(f'indegree {indegree}')
        no_of_nodes_with_indegree_1 = 0
        for i in range(n):
            if indegree[i] == 1:
                no_of_nodes_with_indegree_1 += 1
        
        print(f'no_of_nodes_with_indegree_1: {no_of_nodes_with_indegree_1}')
        
        return max(int(no_of_nodes_with_indegree_1 / 2), 1)