class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, elem in enumerate(nums):
            complement = target - elem
            if elem in seen:
                return [seen[elem], i]
            else:
                seen[elem] = i