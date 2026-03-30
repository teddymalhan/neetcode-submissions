class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1]*n, [1]*n

        for i in range(n):
            if i-1 < 0:
                continue
            prefix[i] = prefix[i-1] * nums[(i-1)]

        for num in prefix:
            print(f"prefix: {num}")


        for i in range(n):
            # n - i = n- 0 = n > n - 2
            if n - i - 1 > n - 2:
                continue
            suffix[n-i-1] = suffix[n-i] * nums[(n-i
            )]
        
        for num in suffix:
            print(f"suffix: {num}")
        
        return [suffix[i]*prefix[i] for i in range(n)]

