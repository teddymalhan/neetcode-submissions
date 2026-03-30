class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1]*n, [1]*n

        for i in range(n):
            if i - 1 < 0:
                continue
            if n - i - 1 > n - 2:
                continue
            
            suffix[n-i-1] = suffix[n-i] * nums[n-i]
            prefix[i] = prefix[i-1] * nums[i-1]

        return [suffix[i]*prefix[i] for i in range(n)]