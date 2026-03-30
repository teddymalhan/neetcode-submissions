class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        length = len(nums)
        def dfs(path: List[int], remaining: List[int]):
            nonlocal res
            if len(path) > length:
                return

            res.add(tuple(sorted(path).copy()))

            if remaining:
                for n in remaining:
                    newpath = path + [n]
                    newremaining = remaining.copy()
                    newremaining.remove(n)
                    dfs(newpath, newremaining)
                    
        dfs([], nums)
        return [list(t) for t in res]