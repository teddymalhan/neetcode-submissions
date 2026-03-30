# the way to think about this is the kth largest is the smallest in k elements.
# if we keep a min heap we can access the smallest in k elements in O(1)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        # O(N) time complexity
        heapq.heapify(nums)
        # this loop will run (n-k) times => O((n-k)*logk)
        while len(self.minHeap) > k:
            # O(logn) time complexity per heappop
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # O(logk)
        heapq.heappush(self.minHeap, val)
        # this will also run with O(logk) (we assume the invariant for k elements always exists)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # O(1) lookup
        return self.minHeap[0]