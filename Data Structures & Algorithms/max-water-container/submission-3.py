class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = lambda x, y: min(heights[x], heights[y])*(y-x)
        l, r = 0, len(heights) - 1
        # as a start
        maxArea = 0
        while l < r:
            maxArea = max(maxArea, area(l, r))
            # move the smaller one
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
            


