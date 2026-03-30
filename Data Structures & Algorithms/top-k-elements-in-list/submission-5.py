class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        # create a list of lists where the higher the index higher the frequency so that there is a natural order
        for num, cnt in freq.items():
            count[cnt].append(num)
        
        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res