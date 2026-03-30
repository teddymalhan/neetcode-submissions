class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 

        def dfs(i, cur, total):
            # base case
            if i >= len(nums) or total > target:
                return
            
            # base case
            if target == total:
                res.append(cur.copy())
                return
            
            dfs(i, cur + [nums[i]], total + nums[i])
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res
        