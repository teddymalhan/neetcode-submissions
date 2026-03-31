class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0]*n
        def dfs(i):
            if i < n and cache[i] != 0:
                return cache[i]
            if i >= n:
                return i == n
            return dfs(i+1) + dfs(i+2)
        return dfs(0)