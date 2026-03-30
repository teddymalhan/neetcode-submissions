class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i would try to approach this with two pointer
        # so the idea is to have l and r at the opposite edges and try to iterate with those

        # nums := [-2, -1, 0, 1, 2]


        nums = sorted(nums)
        print(nums)
        

        res = set()

        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) -1 

            while (l < r):
                if l == i: l += 1
                if r == i: r -= 1

                
                if (nums[i] + nums[l] + nums[r] == 0):
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                
                if (nums[l] + nums[r] < -nums[i]):
                    l += 1
                else:
                    r -= 1

        return [list(l) for l in res]

