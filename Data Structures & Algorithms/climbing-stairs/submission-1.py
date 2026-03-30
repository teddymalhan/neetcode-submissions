from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=128)
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i+1) + dfs(i+2)
        return dfs(0)