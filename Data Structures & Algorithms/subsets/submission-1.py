class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # [1,2,3]
        res = []
        subset = []

        def dfs(i, path):
            if i >= len(nums):
                print(*path)
                res.append(path)
                return
            dfs(i+1, path + nums[i])
            dfs(i+1, path)


        dfs(0, [])
        return res