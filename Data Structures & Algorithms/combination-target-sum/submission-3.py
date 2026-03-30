class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            # 1st base case
            if total == target:
                res.append(curr)
                return
            
            if i >= len(nums) or total > target:
                return

            # two case include the element or not include the element
            dfs(i, curr + [nums[i]], total + nums[i])
            dfs(i+1, curr , total) 
        
        dfs(0, [], 0)
        return res