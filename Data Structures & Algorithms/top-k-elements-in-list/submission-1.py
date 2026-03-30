class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # worst case all elements are unique => O(n)
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        heap = []
        # O(nlogk)
        for num in freq.keys():
            # logk
            heapq.heappush(heap, (freq[num], num))
            # logk()
            if len(heap) > k:
                heapq.heappop(heap)
        # O(k) space
        res = []
        # O(k)*O(logk) = O(klogk)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res