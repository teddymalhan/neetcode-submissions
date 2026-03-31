class Solution:
    def rob(self, nums: List[int]) -> int:
        # top-down dp
        cache = [0]*len(nums)
        def dfs(i):
            if i < len(nums) and cache[i]:
                return cache[i]
            if i >= len(nums):
                return 0
            cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return cache[i]
        
        return max(nums[0] + dfs(1), dfs(2)) - 1
        