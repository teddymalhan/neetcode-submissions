class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n)
        numSet = set(nums)
        longest = 0
        # O(n)
        for num in nums:
            # do it once only for each contiguous set of numbers
            # start from the lowest value
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest