class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1]*len(nums), [1]*len(nums)
        for i in range(len(nums)):
            if i < 1:
                continue
            if i < 1:
                continue 
            prefix[i] = prefix[i-1] * nums[(i)]
            suffix[n-i-1] = suffix[n-i] * nums[n-i]
        
        return [prefix[i] * suffix[i] for i in range(n)]