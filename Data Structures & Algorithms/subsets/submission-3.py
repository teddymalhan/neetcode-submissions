class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(subset: List[int], i:int):
            if i >= len(nums):
                res.append(subset)
                return
            
            dfs(subset+[nums[i]], i+1)
            dfs(subset, i+1)

        dfs([], 0)
        return res