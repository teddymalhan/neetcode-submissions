class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq heappush heappop heapify heap[0] returns the smallest element

        # we choose the two heaviest stones
        # smash them together
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        # get the two heaviest stones
        while len(maxHeap) > 1:
            # largest
            stone1 = -heapq.heappop(maxHeap)
            # second largest
            stone2 = -heapq.heappop(maxHeap)

            # compare the two stones
            if stone1 != stone2:
                heapq.heappush(maxHeap, stone2 - stone1)
        return -maxHeap[0] if maxHeap else 0