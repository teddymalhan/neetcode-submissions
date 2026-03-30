class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # since -nums[i] both l and r will be on the right of nums[i] right
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    res.add((nums[i], nums[l], nums[r]))
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        
        return [list(x) for x in res]