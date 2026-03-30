class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1

        freq = defaultdict(list) 
        for num, frequency in cnt.items():
            freq[frequency].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            while freq[i] and len(res) < k:
                res.append(freq[i].pop())

            if len(res) == k:
                return res

        return res


