class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        suffix = [1]*n

        for i in range(len(nums) - 1):
            prefix[i+1] = prefix[i] * nums[i]
        
        for i in range(len(nums) - 1, 0, -1):
            suffix[i-1] = suffix[i] * nums[i]

        return [x*y for x, y in zip(prefix, suffix)]