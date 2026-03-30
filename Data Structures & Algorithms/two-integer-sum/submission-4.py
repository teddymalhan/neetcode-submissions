class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, elem in enumerate(nums):
            complement = target - elem
            if complement in seen:
                return [seen[complement],i]
            else:
                seen[elem] = i
    