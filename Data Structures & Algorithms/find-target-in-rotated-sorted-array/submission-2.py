class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[l] == target:
                return l
            if nums[mid] == target:
                return mid
            # search this section if it seems within this range
            if nums[l] <= target <= nums[mid]:
                r = mid - 1
            # if it's not in this range then search the other one
            else:
                l = mid + 1
        return -1