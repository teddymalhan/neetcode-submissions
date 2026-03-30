class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # i believe having a max heap makes sense here.
        maxHeap = []
        # only storing the k values so that time complexity is O(nlogk)
        for x,y in points:
            # O(logk)
            heapq.heappush(maxHeap, (-(x**2+y**2), x, y))
            # O(logk)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
                
        return [(x,y) for (_, x, y) in maxHeap]