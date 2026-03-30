class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles[i] <- no. of bananas in i'th pile
        # h <- number of hours you have to eat all the bananas

        # k <- banana eating speed
        # eat k bananas from that pile
        # math.ceil(piles[i]/k) hours per thing
        # sum it all up and check if less than the needed
        # we can start from 1 -> optimal
        def currentSum(k: int) -> int:
            currentSum = 0
            for i, pile in enumerate(piles):
                currentSum += math.ceil(pile/k)
            return currentSum
        
        l, r = 1, max(piles) 
        while l <= r:
            mid = (l + r) // 2
            if currentSum(mid) <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
        