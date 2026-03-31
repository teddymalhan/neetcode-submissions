class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()

        def dfs(i, cur, total):
            # if sum == target
            if total == target:
                res.add(tuple(cur.copy()))
                return 
            
            if total > target or i >= len(candidates):
                return
            
            dfs(i, cur + [candidates[i]], target + nums[i])
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res

