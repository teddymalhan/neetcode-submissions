class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i, elem in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if l == i: l += 1
                if r == i: r -= 1
                if nums[l] + nums[r] == -nums[i]:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                
                if (nums[l] + nums[r] < - nums[i]):
                    l += 1
                else:
                    r -= 1

        return [list(t) for t in res]
                

