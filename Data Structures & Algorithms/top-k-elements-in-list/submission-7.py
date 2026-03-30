from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for i in range(len(nums)):
            cnt[nums[i]]+=1
        
        # we have something like
        # number 2 3 times
        # {2: 3}
        frequency = defaultdict(list)
        for key, freq in cnt.items():
            frequency[freq].append(key)
        
        # we have something like this now
        # 3 frequency for 3 and 2
        # {3: [3,2]}

        # basically we want to run a counter
        res = []
        for i in range(len(nums), 0, -1):
            while frequency[i] and len(res) < k:
                res.append(frequency[i].pop())
            if len(res)==k:
                return res
        
        return res
            