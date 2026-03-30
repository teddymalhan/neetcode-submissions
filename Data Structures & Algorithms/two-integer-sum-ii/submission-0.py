class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if (numbers):
            l, r = 0, len(numbers) - 1
            current_sum = numbers[l] + numbers[r]
            while (l <= r):
                if (current_sum == target):
                    return [l+1, r+1]
                if (current_sum) < target:
                    l += 1
                    current_sum = numbers[l] + numbers[r]
                else:
                    r -= 1
                    current_sum = numbers[l] + numbers[r]
            return None