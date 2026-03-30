class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        for num in numSet:
            currentNum = num
            if (currentNum - 1) not in numSet:
                length = 1
                while currentNum + 1 in numSet:
                    length += 1
                    currentNum += 1
                maxLength = max(length, maxLength)

        return maxLength 
