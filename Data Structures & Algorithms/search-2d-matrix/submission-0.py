class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # the whole idea is you search through the column with binary search find the lower end of the thing
        # then for that row search through that row

        t, b = 0, rows - 1
        while t <= b:
            mid = (t+b) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                b = mid - 1
            else:
                t = mid + 1
        
        # so the b is the right row to search
        l, r = 0, len(matrix[b])
        while l <= r:
            mid = (l+r) // 2
            if matrix[b][mid] == target:
                return True
            if matrix[b][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False