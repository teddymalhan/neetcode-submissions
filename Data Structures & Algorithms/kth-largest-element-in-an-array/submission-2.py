class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(nlogn) Time
        # O(1) Space
        # kth largest -> smallest in a group of k elements
        # min heap
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]