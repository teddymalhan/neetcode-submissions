class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return x**2 + y**2

        # O(n)
        maxHeap = [(-distance(x,y), x,y) for (x,y) in points]
        heapq.heapify(maxHeap)

        # O(klogn)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        
        return [(x,y) for (_, x, y) in mHeap]