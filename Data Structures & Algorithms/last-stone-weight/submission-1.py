class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones] 
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            highest = -heapq.heappop(maxHeap)
            second_highest = -heapq.heappop(maxHeap)

            if highest != second_highest:
                heapq.heappush(maxHeap, second_highest - highest)
        
        return -maxHeap[0] if maxHeap else 0