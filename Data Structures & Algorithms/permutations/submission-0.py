class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        def dfs(path: List[int], remaining: List[int]):
            nonlocal res
            if len(path) == length:
                res.append(path.copy())
                return

            if remaining:
                for n in remaining:
                    newpath = path + [n]
                    newremaining = remaining.copy()
                    newremaining.remove(n)
                    dfs(newpath, newremaining)
                    
        dfs([], nums)
        return res