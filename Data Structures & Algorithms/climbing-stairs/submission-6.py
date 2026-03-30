class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0]*n
        def dfs(i):
            nonlocal cache
            if i < n and cache[i] != 0:
                return cache[i]
            if i >= n:
                return i == n
            cache[i] =  dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)