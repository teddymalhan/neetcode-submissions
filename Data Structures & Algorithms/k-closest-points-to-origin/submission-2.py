class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # i believe having a max heap makes sense here.
        # we want to pop all values that expand beyond the k elements
        # so it makes sense that we pop after k
        maxHeap = [(-(x**2 + y**2), x, y) for (x,y) in points]
        # the k-th closest points to the origin
        # O(N) runtime to heapify
        heapq.heapify(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        # now we have to return all the values to the user
        return [(x,y) for (_, x, y) in maxHeap]