class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1]*26, [1]*26

        for i in range(n):
            if n - i - 1 > n - 2:
                continue
            if i - 1 < 0:
                continue
            
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[n-i-1] = suffix[n-i] * nums[n-i]

        return [suffix[i]*prefix[i] for i in range(n)]