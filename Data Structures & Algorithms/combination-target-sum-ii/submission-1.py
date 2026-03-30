class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = set()
        candidates.sort()
        def dfs(values, index):
            nonlocal res
            sumValues = sum(values) 
            if sumValues == target:
                res.add(tuple(values.copy()))
                return
            
            if index >= n or sumValues > target:
                return
            
            values.append(candidates[index])
            dfs(values, index + 1)
            values.pop()
            dfs(values, index + 1)
        
        dfs([], 0)
        return [list(x) for x in res]