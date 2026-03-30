class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        arr = []
        for num, cnt in freq.items():
            arr.append([cnt, num])
        
        arr.sort(key=lambda x: x[0])

        res = []
        while len(res) < k:
            # from the end
            res.append(arr.pop()[1])
        
        return res

        