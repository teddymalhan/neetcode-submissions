class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap
        # stores 2 as -2
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            # get -2 back use - to convert -2 -> 2
            x = -(heapq.heappop(maxHeap))
            y = -(heapq.heappop(maxHeap))
            if x != y:
                # y - x gives negative value as the normal is x-y (larger - smaller) but a negation of that
                # is y - x
                heapq.heappush(maxHeap,y-x)
            
        if maxHeap:
            return -maxHeap[0]
        else:
            return 0